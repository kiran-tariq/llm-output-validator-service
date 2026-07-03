import json
import time

from pydantic import ValidationError

from app.schemas import SCHEMA_MAP
from app.llm_client import call_llm
from app.metrics import log_validation


def validate_with_retry(
    prompt,
    schema_name,
    max_retries=3
):
    start_time = time.time()

    schema = SCHEMA_MAP[schema_name]

    current_prompt = prompt

    logs = []

    for attempt in range(
        1,
        max_retries + 1
    ):

        raw_response = call_llm(
            current_prompt
        )

        try:

            data = json.loads(
                raw_response
            )

            validated = schema.model_validate(
                data
            )

            latency = (
                time.time() - start_time
            ) * 1000

            log_validation(
                schema_name=schema_name,
                success=True,
                attempts_needed=attempt,
                latency_ms=latency
            )

            return {
                "success": True,
                "attempts": attempt,
                "data": validated.model_dump(),
                "logs": logs
            }

        except (
            json.JSONDecodeError,
            ValidationError
        ) as e:

            error_message = str(e)

            logs.append({
                "attempt": attempt,
                "response": raw_response,
                "error": error_message
            })

            current_prompt = f"""
Your previous response failed validation.

Error:
{error_message}

Return ONLY valid JSON.

Original Task:
{prompt}
"""

    latency = (
        time.time() - start_time
    ) * 1000

    log_validation(
        schema_name=schema_name,
        success=False,
        attempts_needed=max_retries,
        latency_ms=latency,
        error_type="ValidationError"
    )

    return {
        "success": False,
        "logs": logs
    }