from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Lead(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    last_name: str = Field(alias="LastName")
    email: str = Field(alias="Email")
    phone: str = Field(alias="Phone")
    company: str = Field(alias="Company")
    id: Optional[str] = Field(default=None)
    first_name: Optional[str] = Field(default=None, alias="FirstName")

class LeadOut(BaseModel):
    id: str

class LeadOutError(BaseModel):
    status_code: int
    detail: dict | list | str


