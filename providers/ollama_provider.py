import ollama

def call_ollama(prompt: str, model: str = "qwen2.5-coder:7b") -> str:
    """
    Sends a prompt to a local Ollama model and returns the generated text.
    """
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]