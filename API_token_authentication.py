from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
if HUGGINGFACEHUB_API_TOKEN is None:
    raise ValueError("No API_KEY environment variable set")

# Use the api_key for authentication
print(f"API Key: {HUGGINGFACEHUB_API_TOKEN}")
