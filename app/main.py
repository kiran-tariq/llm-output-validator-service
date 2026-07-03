from fastapi import FastAPI
from sqlalchemy import func

from app.validator import validate_with_retry
from app.database import SessionLocal
from app.models import ValidationLog

app = FastAPI(
    title="LLM Output Validator"
)


@app.post("/validate")
def validate(payload: dict):

    return validate_with_retry(
        prompt=payload["prompt"],
        schema_name=payload["schema_name"]
    )


@app.get("/metrics")
def metrics():

    db = SessionLocal()

    total_calls = db.query(
        ValidationLog
    ).count()

    successful = db.query(
        ValidationLog
    ).filter(
        ValidationLog.success == True
    ).count()

    avg_attempts = db.query(
        func.avg(
            ValidationLog.attempts_needed
        )
    ).scalar()

    error_rows = db.query(
        ValidationLog.error_type
    ).filter(
        ValidationLog.error_type != None
    ).all()

    db.close()

    success_rate = 0

    if total_calls:
        success_rate = (
            successful /
            total_calls
        ) * 100

    common_errors = {}

    for row in error_rows:

        error = row[0]

        common_errors[error] = (
            common_errors.get(error, 0) + 1
        )

    return {
        "total_calls": total_calls,
        "successful_calls": successful,
        "success_rate": round(
            success_rate,
            2
        ),
        "average_attempts": round(
            avg_attempts or 0,
            2
        ),
        "common_errors": common_errors
    }


@app.get("/schemas")
def schemas():

    return {
        "schemas": {
            "sentiment": {
                "fields": [
                    "sentiment",
                    "confidence",
                    "explanation"
                ]
            },
            "task_extraction": {
                "fields": [
                    "tasks"
                ]
            },
            "content_summary": {
                "fields": [
                    "title",
                    "summary",
                    "key_points"
                ]
            }
        }
    }
