from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_content(topic, product, audience, tone):
    prompt = ( f"""
    You are an expert content creator for LinkedIn.
    Write a {tone} LinkedIn post about engaging LinkedIn post about {topic} 
    to promote {product}, tailored for {audience}. 
    
    Guidelines:
    - Hook with a strong first sentence.
    - Keep it concise (150–250 words).
    - Use short paragraphs or bullet points for readability.
    - Add a call to action at the end.
    - Do not use hashtags or emojis.
    -Make it concise, insightful, and include a call to action

    """
)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
