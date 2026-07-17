# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def call_gemini(prompt: str, model: str = "gemini-1.5-flash") -> str:
#     """
#     Sends a prompt to Google's Gemini API and returns the generated text.
#     """
#     gemini_model = genai.GenerativeModel(model)
#     response = gemini_model.generate_content(prompt)
#     return response.text


import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str, model: str = "gemini-2.0-flash") -> str:
    """
    Sends a prompt to Google's Gemini API and returns the generated text.
    """
    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    return response.text