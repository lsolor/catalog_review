from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    sku: str


class ProductRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float | None = None
    sku: str

    class Config:
        from_attributes = True
