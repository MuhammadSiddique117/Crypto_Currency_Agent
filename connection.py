from dotenv import load_dotenv
import requests
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# ✅ Load environment variables from .env file
load_dotenv()

# 🔐 Get the Gemini API key securely from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ❌ Do NOT print the API key in production
# print("Gemini API Key:", gemini_api_key)  # Uncomment ONLY for debugging

# 🛡️ Validate the key is present
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# ✅ Use the key to configure the external OpenAI-compatible client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# ✅ Define the model configuration
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ✅ Create the run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
