from uuid import uuid4
from .security import s3_connection
from fastapi import UploadFile
from typing import List

s3 = s3_connection()


def upload(files: List[UploadFile]):
    url = []
    for i in files:
        name = i.filename + str(uuid4())

        s3.upload_fileobj(
            i.file,
            'new-trash',
            name,
            ExtraArgs={"ACL": "public-read",
                       "ContentType": i.content_type}
        )
        url.append(f'https://new-trash.s3.ap-northeast-2.amazonaws.com/{name}')

    return {
        'url': url
    }
