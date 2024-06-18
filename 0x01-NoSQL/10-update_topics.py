#!/usr/bin/env python3
"""Change school topics """

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
        a Python function that changes all topics of
        a school document based on the name
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": list(topics)}})


if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)
