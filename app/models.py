from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class ValidationLog(Base):

    __tablename__ = "validation_logs"

    id = Column(Integer, primary_key=True)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    schema_name = Column(String)

    success = Column(Boolean)

    attempts_needed = Column(Integer)

    latency_ms = Column(Float)

    error_type = Column(String, nullable=True)