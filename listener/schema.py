from datetime import datetime, timezone
from dataclasses import dataclass, asdict


@dataclass
class Interaction:
    """
    Represents a single logged interaction with the coding agent.
    """
    timestamp: str
    prompt: str
    generated_code: str
    provider: str
    validation_passed: bool = None
    validation_errors: str = None
    response_time_seconds: float = None

    def to_dict(self) -> dict:
        return asdict(self)


def new_interaction(prompt: str, generated_code: str, provider: str,
                     response_time_seconds: float = None) -> Interaction:
    """
    Convenience constructor that auto-fills the timestamp.
    """
    return Interaction(
        timestamp=datetime.now(timezone.utc).isoformat(),
        prompt=prompt,
        generated_code=generated_code,
        provider=provider,
        response_time_seconds=response_time_seconds,
    )