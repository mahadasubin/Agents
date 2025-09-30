from fastapi import FastAPI
from pydantic import BaseModel
#from agent import generate_linkedin_post
from content_agent import generate_content
from image_agent import fetch_images

app = FastAPI()

class PostRequest(BaseModel):
    topic: str
    audience: str = "tech professionals"
    #tone: str = "professional"
    product: str

@app.post("/generate")
def generate_post(req: PostRequest):
    # post = generate_linkedin_post(req.topic, req.audience, req.tone)
    content = generate_content(req.topic, req.product, req.audience)
    images = fetch_images(req.topic + " " + req.product)
    return {"content": content, "images": images}
    # return {"post": post}
