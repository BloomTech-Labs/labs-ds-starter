from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import MongoDB
from app.validation import User, UserQuery, UserUpdate
from app.validation import default_query, default_update, default_user


API = FastAPI(
    title="BloomTech Labs DS API Template",
    version="0.0.1",
    docs_url="/",
)
API.db = MongoDB()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def api_version():
    """ Returns current API version
    @return: String Version """
    return API.version


@API.post("/create-user")
async def create_user(user: User = default_user):
    """ Creates one user
    @param user: User
    @return: Boolean Success """
    return API.db.create(user.dict(exclude_none=True))


@API.put("/read-users")
async def read_users(user_query: UserQuery = default_query):
    """ Returns array of all matched users
    @param user_query: UserQuery
    @return: Array[User] """
    return API.db.read(user_query.dict(exclude_none=True))


@API.patch("/update-users")
async def update_users(user_query: UserQuery = default_query,
                       user_update: UserUpdate = default_update):
    """ Updates all matched users
    @param user_query: UserQuery
    @param user_update: UserUpdate
    @return: Boolean Success """
    return API.db.update(
        user_query.dict(exclude_none=True),
        user_update.dict(exclude_none=True),
    )


@API.delete("/delete-users")
async def delete_users(user_query: UserQuery = default_query):
    """ Deletes all matched users
    @param user_query: UserQuery
    @return: Boolean Success """
    return API.db.delete(user_query.dict(exclude_none=True))
