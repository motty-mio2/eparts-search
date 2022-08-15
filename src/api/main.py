import pathlib
import subprocess
import sys
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sites.sengoku import sengoku

subprocess.run(["playwright", "install", "chromium"])
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def Hello():
    return {"Hello": "World!"}


class query(BaseModel):
    len: int
    keywords: list[str]


@app.get("/search")
def Search(item: query):
    s = sengoku()
    return s.search(item.keywords)


@app.get("/test/")
def test(query: Optional[str] = None):
    if query is not None:
        return query.split(" ") * 2
    return None


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=4000, reload=True)  # type:ignore


if __name__ == "__main__":
    main()
