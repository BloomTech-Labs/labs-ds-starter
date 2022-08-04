""" MongoDB Interface """
from os import getenv
from typing import Optional, List, Dict, Iterable

from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv


class MongoDB:
    """ DocTests
    >>> db = MongoDB()
    >>> db.create({"Test": True})
    True
    >>> db.read({"Test": True})
    [{'Test': True}]
    >>> db.update({"Test": True}, {"New Field": True})
    True
    >>> db.read({"Test": True})
    [{'Test': True, 'New Field': True}]
    >>> db.delete({"Test": True})
    True
    >>> db.read({"Test": True})
    []
    """
    load_dotenv()

    def _collection(self) -> Collection:
        """ Connects to the MongoDB Collection
        @return: Collection """
        return MongoClient(
            getenv("MONGO_URL")
        )[getenv("MONGO_DB")][getenv("MONGO_COLLECTION")]

    def create(self, data: Dict) -> bool:
        """ Creates one record in the Collection
        @param data: Dict
        @return: Boolean Success """
        return self._collection().insert_one(dict(data)).acknowledged

    def create_many(self, data: Iterable[Dict]) -> bool:
        """ Creates many records in the Collection
        @param data: Iterable[Dict]
        @return: Boolean Success """
        return self._collection().insert_many(map(dict, data)).acknowledged

    def read(self, query: Optional[Dict] = None) -> List[Dict]:
        """ Returns a list of records from the collection
        @param query: Dict
        @return: List[Dict] """
        return list(self._collection().find(query, {"_id": False}))

    def update(self, query: Dict, update_data: Dict) -> bool:
        """ Updates the matched records with new data
        @param query: Dict
        @param update_data: Dict
        @return: Boolean Success """
        return self._collection().update_many(
            query, {"$set": update_data}
        ).acknowledged

    def delete(self, query: Dict) -> bool:
        """ Deletes the matched records
        @param query: Dict
        @return: Boolean Success """
        return self._collection().delete_many(query).acknowledged
