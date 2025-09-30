from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_linkedin_post(topic, audience="tech professionals", tone="professional"):
    """
    Generate a LinkedIn post about a given topic.
    """
    prompt = f"""
    You are an expert content creator for LinkedIn.
    Write a {tone} LinkedIn post about: "{topic}".
    Target audience: {audience}.
    
    Guidelines:
    - Hook with a strong first sentence.
    - Keep it concise (150–250 words).
    - Use short paragraphs or bullet points for readability.
    - Add a call to action at the end.
    - Do not use hashtags or emojis.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # you can switch to gpt-4.1 or gpt-3.5
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
