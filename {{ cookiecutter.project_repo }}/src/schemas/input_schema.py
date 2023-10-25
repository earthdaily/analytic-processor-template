from pydantic import BaseModel, Field
from typing import List, Optional

class Season(BaseModel):
    season_duration: int
    season_start_day: int
    season_start_month: int

class Parameter(BaseModel):
    start_date: str
    end_date: str
    country_code: str
    season: Optional[Season]
    historical: bool

class Data(BaseModel):
    id: str
    crop: str
    year: int
    feature: str

#
class input_Model(BaseModel):
    parameters: Parameter
    data: List[Data]

    class Config:
        extra = "forbid"