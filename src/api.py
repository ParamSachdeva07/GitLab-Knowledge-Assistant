from fastapi import FastAPI, BackgroundTasks, HTTPException, Request
from pydantic import BaseModel, Field
import asyncio

from src.retrieval.top_k_chunks import retrieve
from src.retrieval.response import getResponse
from src.chunking.incremental_loader import sync_changes

import json
import logging
from uuid import uuid4

app = FastAPI()

PROJECT_ID = 123456

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


def run_sync():
    try:
        sync_changes()
    except Exception:
        logger.exception("Webhook-triggered ingestion failed")


@app.post('/webhooks/gitlab')
async def gitlab_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):
    event = request.headers.get("X-Gitlab-Event")

    if event != "Push Hook":
        return {"status": "ignored", "reason": "not a push"}

    payload = await request.json()

    if payload.get("project", {}).get("id") != PROJECT_ID:
        raise HTTPException(status_code=403, detail="Unexpected proejct")

    if payload.get("ref") != "refs/heads/main":
        return {"status": "ignored", "reason": "not main"}

    background_tasks.add_task(run_sync)

    return {"status": "accepted"}
        