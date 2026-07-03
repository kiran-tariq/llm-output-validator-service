import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

from app.validator import (
    validate_sentiment
)


good_response = """
{
    "sentiment":"positive",
    "confidence":0.95,
    "explanation":"Very positive review"
}
"""

bad_response = """
{
    "sentiment":"good"
}
"""


print("GOOD RESPONSE")
print(
    validate_sentiment(
        good_response
    )
)

print("\nBAD RESPONSE")
print(
    validate_sentiment(
        bad_response
    )
)