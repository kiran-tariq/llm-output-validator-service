from typing import Literal
from pydantic import BaseModel, Field


class SentimentResult(BaseModel):
    sentiment: Literal[
        "positive",
        "negative",
        "neutral"
    ]

    confidence: float = Field(
        ge=0,
        le=1
    )

    explanation: str


SCHEMA_MAP = {
    "sentiment": SentimentResult
}