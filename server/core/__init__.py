from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from server.config import MySQL


@contextmanager
def session_scope():
    engine = create_engine(
        url=MySQL.MY_SQL_URL,
        pool_recycle=3600,
        pool_size=20,
        max_overflow=20,
        pool_pre_ping=True
    )
    session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


Base = declarative_base()
