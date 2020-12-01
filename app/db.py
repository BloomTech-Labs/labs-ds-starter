"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter
from sqlalchemy import create_engine

load_dotenv()
database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
engine = create_engine(database_url)
router = APIRouter()


@router.get('/info')
async def get_url():
    """Verify we can connect to the database, 
    and return the database URL, in this format:

    dialect://user:password@host/dbname
    """
    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()
        return {'url': url_without_password}
