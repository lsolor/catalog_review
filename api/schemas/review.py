from pydantic import BaseModel


class ReviewCreate(BaseModel):
    product_id: int
    user_id: int
    rating: int
    comment: str | None = None


class ReviewRead(BaseModel):
    id: int
    product_id: int
    user_id: int
    rating: int
    comment: str | None = None

    class Config:
        from_attributes = True
