from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.retrieval.top_k_chunks import retrieve
from src.retrieval.response import getResponse

app = FastAPI()

class RetrievalRequest(BaseModel):
    query: str = Field(min_length=1)
    k: int = Field(default=10, ge=1, le=20)

class Answer(BaseModel):
    query: str = Field(min_length=1)
    k: int = Field(default=10, ge=1, le=20)

@app.post('/retrieve_chunks')
def retrieve_chunks(request: RetrievalRequest):
    results = retrieve(request.query, k=request.k)
    return {'results': results}

@app.post('/answer')
def answer(request: Answer):
    results = getResponse(request.query, k = request.k)
    return {'results': results}


