#!/usr/bin/env python3
"""List all documentation"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
        function list all documentation
    """
    documents = mongo_collection.find()
    return list(documents)


if __name__ == "__main__":
    list_all(mongo_collection)
