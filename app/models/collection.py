from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class CollectionModel(BaseModel):
    dataSource: str = Field(..., example="mongodb")
    database: str = Field(..., example="todo")
    collection: str = Field(..., example="tasks")
    filter: dict = Field(..., example={"text": "Do the dishes"})
    projection: Optional[dict] = Field(None, example={"status": 1, "text": 1})

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
                    "text": "Do the dishes"
                },
                "projection": {
                    "status": 1,
                    "text": 1
                }
            }
        }

class CollectionFind(BaseModel):
    dataSource: str = Field(..., example="mongodb")
    database: str = Field(..., example="todo")
    collection: str = Field(..., example="tasks")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "dataSource": "mongodb",
                "database": "todo",
                "collection": "tasks"
            }
        }


class CollectionInsert(BaseModel):
    dataSource: str = Field(..., example="mongodb")
    database: str = Field(..., example="todo")
    collection: str = Field(..., example="tasks")
    document: dict = Field(..., example={"text": "Do the dishes"})

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "dataSource": "mongodb",
                "database": "todo",
                "collection": "tasks",
                "document": {
                    "text": "Do the dishes"
                }
            }
        }


class CollectionInsertMany(BaseModel):
    dataSource: str = Field(..., example="mongodb")
    database: str = Field(..., example="todo")
    collection: str = Field(..., example="tasks")
    document: list = Field(..., example={"text": "Do the dishes"})

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "dataSource": "mongodb",
                "database": "todo",
                "collection": "tasks",
                "document": [{
                    "text": "Do the dishes"
                },
                {
                    "another text" : "Wash the clothes"
                }]
            }
        }