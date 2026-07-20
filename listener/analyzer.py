import json
import os
from collections import Counter

LOG_FILE = os.path.join("logs", "interactions.jsonl")


def load_interactions() -> list[dict]:
    """Reads all logged interactions from the JSONL file."""
    if not os.path.exists(LOG_FILE):
        return []

    interactions = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                interactions.append(json.loads(line))
    return interactions


def validation_pass_rate(interactions: list[dict]) -> float:
    """Returns the percentage of interactions that passed validation."""
    validated = [i for i in interactions if i.get("validation_passed") is not None]
    if not validated:
        return 0.0
    passed = sum(1 for i in validated if i["validation_passed"])
    return round((passed / len(validated)) * 100, 1)


def average_response_time(interactions: list[dict]) -> float:
    """Returns the average response time across all interactions."""
    times = [i["response_time_seconds"] for i in interactions if i.get("response_time_seconds")]
    if not times:
        return 0.0
    return round(sum(times) / len(times), 2)


def common_keywords(interactions: list[dict], top_n: int = 5) -> list[tuple[str, int]]:
    """
    Finds the most common meaningful words across all prompts.
    A very simple frequency count, ignoring common filler words.
    """
    stopwords = {"a", "the", "to", "write", "function", "that", "of", "using", "an", "in"}
    counter = Counter()
    for i in interactions:
        words = i.get("prompt", "").lower().split()
        for w in words:
            w = w.strip(".,!?")
            if w and w not in stopwords:
                counter[w] += 1
    return counter.most_common(top_n)


def provider_breakdown(interactions: list[dict]) -> dict:
    """Counts how many interactions used each provider."""
    return dict(Counter(i.get("provider", "unknown") for i in interactions))


def print_summary():
    interactions = load_interactions()
    print(f"Total interactions logged: {len(interactions)}\n")
    print(f"Validation pass rate: {validation_pass_rate(interactions)}%")
    print(f"Average response time: {average_response_time(interactions)}s")
    print(f"Provider breakdown: {provider_breakdown(interactions)}")
    print(f"Most common keywords in requests: {common_keywords(interactions)}")


if __name__ == "__main__":
    print_summary()