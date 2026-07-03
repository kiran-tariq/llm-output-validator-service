import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from app.validator import (
    validate_with_retry
)

prompt = """
Return ONLY valid JSON.

Analyze sentiment:

'I absolutely loved this product.'

Required fields:

{
  "sentiment": "positive|negative|neutral",
  "confidence": 0.0-1.0,
  "explanation": "string"
}
"""

result = validate_with_retry(
    prompt=prompt,
    schema_name="sentiment"
)

print(result)