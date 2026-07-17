from providers.ollama_provider import call_ollama
from providers.gemini_provider import call_gemini

def call_llm(prompt: str, provider: str = "ollama") -> str:
    """
    Routes a prompt to the chosen LLM provider.
    provider: "ollama", "gemini", or "claude"
    """
    if provider == "ollama":
        return call_ollama(prompt)
    elif provider == "gemini":
        return call_gemini(prompt)
    else:
        raise ValueError(f"Unknown provider: {provider}")