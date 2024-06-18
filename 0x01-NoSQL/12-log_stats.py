#!/usr/bin/env python3
"""Log state"""

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient('localhost', 27017)
    db_logs = client['logs']
    collection_nginx = db_logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(collection_nginx.estimated_document_count()))
    print("Methods:")

    for method in methods:
        num_docs = collection_nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, num_docs))

    status = collection_nginx.count_documents(
                 {"method": "GET", "path": "/status"})
    print("{} status check".format(status))
