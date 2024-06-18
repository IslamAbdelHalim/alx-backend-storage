#!/usr/bin/env python3
"""Insert a document in python"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
        insert a document in python
    """
    inserted_id = mongo_collection.insert_one(kwargs).inserted_id
    return inserted_id


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
