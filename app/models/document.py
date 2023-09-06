from typing import Optional

from pydantic import BaseModel


class Document(BaseModel):
    _id: Optional[str]
    status: Optional[str]
    text: Optional[str]
    error: Optional[str]
    error_code: Optional[str]
    link: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "6193504e1be4ab27791c8133",
                "status": "open",
                "text": "Do the dishes"
            }
        }