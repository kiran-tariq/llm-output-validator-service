from app.database import SessionLocal
from app.models import ValidationLog


def log_validation(
    schema_name,
    success,
    attempts_needed,
    latency_ms,
    error_type=None
):
    db = SessionLocal()

    log = ValidationLog(
        schema_name=schema_name,
        success=success,
        attempts_needed=attempts_needed,
        latency_ms=latency_ms,
        error_type=error_type
    )

    db.add(log)
    db.commit()
    db.close()


def get_metrics():
    db = SessionLocal()

    logs = db.query(ValidationLog).all()

    total_calls = len(logs)

    if total_calls == 0:
        return {
            "total_calls": 0
        }

    successful = [l for l in logs if l.success]

    success_rate = (
        len(successful) / total_calls
    ) * 100

    avg_attempts = (
        sum(l.attempts_needed for l in logs)
        / total_calls
    )

    error_counts = {}

    for log in logs:
        if log.error_type:
            error_counts[log.error_type] = (
                error_counts.get(log.error_type, 0) + 1
            )

    db.close()

    return {
        "total_calls": total_calls,
        "success_rate": round(success_rate, 2),
        "average_attempts": round(avg_attempts, 2),
        "common_errors": error_counts
    }