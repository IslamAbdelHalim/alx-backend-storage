#!/usr/bin/env python3
"""Where can I learn Python? """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    a Python function that returns the list of school having a specific topic
    """
    docs = mongo_collection.find({"topics": topic})
    return docs


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
