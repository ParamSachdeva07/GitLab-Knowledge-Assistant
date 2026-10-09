from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.retrieval.top_k_chunks import retrieve
from src.retrieval.response import getResponse

import json
import logging
from uuid import uuid4

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RetrievalRequest(BaseModel):
    query: str = Field(min_length=1)
    k: int = Field(default=5, ge=1, le=20)

class Answer(BaseModel):
    query: str = Field(min_length=1)
    k: int = Field(default=5, ge=1, le=20)

@app.post('/retrieve_chunks')
def retrieve_chunks(request: RetrievalRequest):
    results = retrieve(request.query, k=request.k)
    return {'results': results}

@app.post('/answer')
def answer(request: Answer):
    request_id = str(uuid4())

    try:
        results = getResponse(request.query, k = request.k)
    except Exception:
        logger.exception(
            json.dumps({
                "event": "answer_failed",
                "request_id": request_id,
                "requested_k": request.k
            })
        )
        raise

    logger.info(
        json.dumps({
            "event": "answer completed",
            "request_id": request_id,
            "requested_k": request.k,
            "returned_chunks": len(results["chunks"]),
            "timings_ms": results["timings_ms"],
            "chunk_ids": [chunk["id"] for chunk in results["chunks"]]
        })
    )
    return {
        "request_id": request_id,
        'results': results
        }

