from pydantic import BaseModel


class DestinationBase(BaseModel):
    city: str
    country: str
    description: str = ""


class DestinationCreate(DestinationBase):
    pass


class DestinationUpdate(BaseModel):
    city: str | None = None
    country: str | None = None
    description: str | None = None


class Destination(DestinationBase):
    id: int

    model_config = {"from_attributes": True}
