from groq import Groq
import os

clent = Groq(
    api_key = os.environ.get("GROQ_API_KEY"),
)
