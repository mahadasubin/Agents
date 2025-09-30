from fastapi import FastAPI
from pydantic import BaseModel
from content_agent import generate_content
from image_agent import fetch_images

app = FastAPI()

class PostRequest(BaseModel):
    topic: str
    audience: str = "tech professionals"
    tone: str = "professional"
    product: str

@app.post("/generate")
def generate_post(req: PostRequest):
    content = generate_content(req.topic, req.product, req.audience, req.tone)
    images = fetch_images(req.topic, req.product, req.audience)
    return {"content": content, "images": images}
    
