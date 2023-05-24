import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class MySQL:
    MY_SQL_URL: str = os.getenv("MY_SQL_URL")


class SECURITY:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("algorithm")
    access_time: int = int(os.getenv("access_time"))
