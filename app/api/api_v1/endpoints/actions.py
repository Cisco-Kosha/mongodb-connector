import json
from typing import Any, List, Optional

from bson import json_util
from fastapi import APIRouter, Depends, HTTPException, UploadFile, FastAPI, File, Body
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from starlette import status
from starlette.responses import JSONResponse

from app.core.config import Settings, logger
from app.models.collection import *
from app.models.document import Document, UpdateDocument

from app.utils import exception, logging, helper

router = APIRouter()

settings = Settings()

client = MongoClient(settings.uri)

@router.post("/find", response_model=Any,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def find(body: CollectionFind = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].find()
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/findOne", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def find_one_document(body: CollectionModel = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].find_one(filter=document_metadata['filter'])
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/insertOne", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def insert_one_document(body: CollectionInsert = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].insert_one(document_metadata['document']).inserted_id
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/insertMany", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def insert_many_document(body: CollectionInsertMany = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        for i in range(len(document_metadata['document'])):
            single_doc = db[document_metadata['collection']].insert_one(document_metadata['document'][i]).inserted_id
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/updateOne", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def update_one_document(body: UpdateDocument = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].find_one_and_update(filter=document_metadata['filter'],
                                                                             update=document_metadata['update'],
                                                                             upsert=document_metadata['upsert'])
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/updateMany", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def update_many_document(body: UpdateDocument = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        all_doc = db[document_metadata['collection']].update_many(filter=document_metadata['filter'],
                                                                 update=document_metadata['update'])
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(all_doc.modified_count)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/deleteOne", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def delete_one_document(body: CollectionModel = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].find_one_and_delete(filter=document_metadata['filter'])
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/deleteMany", response_model=Document,
             responses={200: {"model": Any}, 400: {"model": exception.HTTPError}})
def delete_many_document(body: CollectionModel = Body(...)):
    try:
        document_metadata = jsonable_encoder(body)
        db = client[document_metadata['database']]
        single_doc = db[document_metadata['collection']].delete_many(filter=document_metadata['filter'])
        return JSONResponse(status_code=status.HTTP_200_OK, content=json.loads(json_util.dumps(single_doc)))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/listCollections/{databaseName}", response_model=Any)
def list_collections(databaseName: str):
    try:
        db = client[databaseName]
        return JSONResponse(content=db.list_collection_names(), status_code=status.HTTP_200_OK)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/listDatabases", response_model=Any)
def list_databases():
    db = client.list_databases()
    return JSONResponse(content=json.loads(json_util.dumps(db)), status_code=status.HTTP_200_OK)
