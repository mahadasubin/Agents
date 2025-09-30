"""import requests

def fetch_images(query):
    # Example: Unsplash API
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id=jdDwVPdF3fRykN7HtKkSn3n5XmO1XnlycUoI1qcDuTc"
    resp = requests.get(url)
    data = resp.json()
    print(data)
    return [img['urls']['regular'] for img in data['results'][:3]] """

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_images(topic, product, audience):
    prompt = ( f"""
    You are an expert content creator for LinkedIn.
    Generate an image of {product} in the topic {topic} 
    to promote and tailored for {audience}. 
    """
)
    response = client.images.generate(
        model="dall-e-3",  # 'gpt-image-1', 'gpt-image-1-mini', 'gpt-image-0721-mini-alpha', 'dall-e-2', and 'dall-e-3'
        prompt=prompt,
        size='1024x1024'
    )

    # Extract image URL
    image_url = response.data[0].url
    print(image_url)
    # Send it back to Node
    return image_url