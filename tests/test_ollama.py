import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.llm_client import call_llm


response = call_llm(
    "Say hello in one short sentence."
)

print(response)