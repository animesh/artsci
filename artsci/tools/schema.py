from pydantic import BaseModel
class ArtSci(BaseModel):
    topic: str
    types: str
    creation: str
    quantity: float
    quality: str
