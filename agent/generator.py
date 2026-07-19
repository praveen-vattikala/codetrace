import re
from providers import call_llm
from config import DEFAULT_PROVIDER

CODE_GEN_INSTRUCTIONS = """ You are the professionla coding assistant.
Given a request, respond with only the code that fulfils it.
Do not include explanatations, comments about what the code does, or markdown headers.
Wrap th ecode in a single markdown code block using backticks.
"""

def generate_code(request: str, provider: str = None) -> str:
    """
    Generate code for a given request using the configured LLM provider.
    Returns clean code (no explanations, no markdown fences).
    """

    provider = provider or DEFAULT_PROVIDER
    full_prompt = f"{CODE_GEN_INSTRUCTIONS}\n\nRequest: {request}"

    raw_response = call_llm(full_prompt, provider=provider)
    return _extract_code(raw_response)


def _extract_code(text: str) -> str:
    """
    Strips markdown code fences from a model's response, if present.
    Falls backt to returning the raw text if no fences are found.
    """

    match = re.search(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()