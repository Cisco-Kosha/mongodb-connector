from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


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


class UpdateDocument(BaseModel):
    dataSource: Optional[str] = Field(..., example="mongodb")
    database: Optional[str] = Field(..., example="todo")
    collection: Optional[str] = Field(..., example="tasks")
    filter: dict = Field(..., example={"_id": {"$oid": "642f1bb5cee4111898828bf6"}})
    update: dict = Field(..., example={"$set": {"status": "complete"}})
    upsert: Optional[bool] = Field(..., example=False)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "dataSource": "mongodb",
                "database": "todo",
                "collection": "tasks",
                "filter": {
                    "_id": {
                        "$oid": "642f1bb5cee4111898828bf6"
                    }
                },
                "update": {
                    "$set": {
                        "status": "complete"
                    }
                },
                "upsert": False
            }
        }