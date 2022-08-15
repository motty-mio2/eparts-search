import dataclasses

from pydantic import BaseModel


@dataclasses.dataclass
class item(BaseModel):
    name: str
    available: bool
    description: str
    price: int | None
    link: str
    img: str | None
