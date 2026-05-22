from pydantic import BaseModel, Field, field_validator
from typing import List


class WeatherReport(BaseModel):
    city: str
    temperature_c: float = Field(ge=-50, le=60)
    humidity: int = Field(ge=0, le=100)
    conditions: List[str]

  
    @field_validator("city")
    @classmethod
    def city_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("city must be a non-empty string")
        return v