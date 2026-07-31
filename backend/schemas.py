from pydantic import BaseModel


class Laptop(BaseModel):
    brand: str
    model: str
    processor: str
    ram: str
    storage: str
    price: float
    status: str
