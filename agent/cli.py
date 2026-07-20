import sys
import time

from agent.generator import generate_code
from agent.validator import validate_code
from listener.schema import new_interaction
from listener.logger import log_interaction
from config import DEFAULT_PROVIDER


def run(request: str, provider: str = None):
    provider = provider or DEFAULT_PROVIDER

    print(f"\nGenerating code for: \"{request}\" (provider: {provider})...\n")

    start = time.time()
    code = generate_code(request, provider=provider)
    elapsed = time.time() - start

    passed, errors = validate_code(code)

    entry = new_interaction(
        prompt=request,
        generated_code=code,
        provider=provider,
        response_time_seconds=round(elapsed, 2),
    )
    entry.validation_passed = passed
    entry.validation_errors = errors
    log_interaction(entry)

    print("Generated code:\n")
    print(code)
    print()
    if passed:
        print("✅ Validation passed")
    else:
        print("❌ Validation failed:\n")
        print(errors)
    print(f"\n(took {elapsed:.2f}s, logged to logs/interactions.jsonl)\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 -m agent.cli \"your coding request\"")
        sys.exit(1)

    user_request = sys.argv[1]
    run(user_request)