from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_content(topic, product, audience):
    prompt = (
    f"Write a professional, engaging LinkedIn post about {topic} "
    f"to promote {product}, tailored for {audience}. "
    "Make it concise, insightful, and include a call to action."
)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
