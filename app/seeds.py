""" Run this script to reset and reseed the database """
from app.database import MongoDB
from app.generators import RandomUser


def reset_database(mongo: MongoDB) -> bool:
    """ Resets the database by deleting all records in the collection
    @param mongo: MongoDB Interface
    @return: Boolean Success """
    return mongo.delete({})


def seed_database(mongo: MongoDB, count: int) -> bool:
    """ Seeds the collection with random data
    @param mongo: MongoDB Interface
    @param count: Integer, number of records to create
    @return: Boolean Success """
    return mongo.create_many(vars(RandomUser()) for _ in range(count))


if __name__ == '__main__':
    db = MongoDB()
    reset_database(db)
    seed_database(db, 1000)
