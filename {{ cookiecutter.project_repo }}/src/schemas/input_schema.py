from pydantic import BaseModel, Field
from typing import List, Optional

class Parameter(BaseModel):
    season_duration: int
    season_start_day: int
    season_start_month: int
    historical: bool

class DataItem(BaseModel):
    id: Optional[str]
    crop: Optional[str]
    year: Optional[int]
    feature: Optional[str]

class InputModel(BaseModel):
    parametersProfile: str
    parameters: Parameter
    data: List[DataItem]
