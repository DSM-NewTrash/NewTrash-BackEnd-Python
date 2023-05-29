from typing import List

from server.core import session_scope
from fastapi import APIRouter, UploadFile, File

from ..utill.image import upload


app = APIRouter(prefix="/image")


@app.post("")
async def image(files: List[UploadFile] = File()):
    return upload(files=files)
