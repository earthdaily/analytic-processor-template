from pydantic import BaseModel, HttpUrl, ValidationError

class Metadata(BaseModel):
    generated_timestamp: str
    duration_seconds: float
    datacube_format: str  # "zarr", "netcdf"

class ProcessOutput(BaseModel):
    status: str
    datacube_url: HttpUrl
    metadata: Metadata
    error: str = None
