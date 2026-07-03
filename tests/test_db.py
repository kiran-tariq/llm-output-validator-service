from app.database import SessionLocal
from app.models import ValidationLog

db = SessionLocal()

logs = db.query(ValidationLog).all()

print(f"Total Logs: {len(logs)}")

for log in logs:
    print(
        log.id,
        log.schema_name,
        log.success,
        log.attempts_needed
    )

db.close()