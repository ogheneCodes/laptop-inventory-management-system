from typing import Literal

from pydantic import BaseModel, Field


class Laptop(BaseModel):
    brand: str = Field(..., min_length=2, max_length=50)

    model: str = Field(..., min_length=2, max_length=100)

    processor: str = Field(..., min_length=2, max_length=100)

    ram: str = Field(..., min_length=2, max_length=30)

    storage: str = Field(..., min_length=2, max_length=30)

    price: float = Field(..., gt=0)

    status: Literal["Available", "Reserved", "Sold Out"]
