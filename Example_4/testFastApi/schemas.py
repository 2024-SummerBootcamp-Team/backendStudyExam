from pydantic import BaseModel


class MemberCreate(BaseModel):
    name: str


class MemberResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
