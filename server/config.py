import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class MySQL:
    MY_SQL_URL: str = os.getenv("MY_SQL_URL")


class SECURITY:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("algorithm")
    access_time: int = int(os.getenv("access_time"))
    aws_access_key: str = os.getenv('aws_access_key')
    aws_secret_key: str = os.getenv('aws_secret_access_key')
    region: str = os.getenv('region_name')
    user_default_image: str = os.getenv('user_default_image')
