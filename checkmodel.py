import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

# List available models
models = client.models.list()

# Print all model IDs
print("✅ Available OpenAI Models:")
for model in models.data:
    print("-", model.id)
