from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

# class MetadataRequest(BaseModel):
#     id: Optional[UUID]
#     client_name: str
#     file_name: str
#     file_content: str
#     metadata: str
#     created_by: str
#     updated_by: str
#     created_on: str
#     updated_on: str

class MetadataRequest(BaseModel):
    # id: Optional[UUID]
    client_name: str
    file_name: str
    file_content: str

    class Config:
        from_attributes = True

class MetadataResponse(BaseModel):
    id: Optional[UUID]
    client_name: str
    file_name: str
    file_content: str
    # response_metadata: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    created_on: datetime
    updated_on: datetime

    class Config:
        from_attributes = True