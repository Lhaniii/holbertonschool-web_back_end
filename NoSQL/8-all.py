#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Collection"""
    collection = mongo_collection.find()
    if not collection:
        return []
    else:
        return collection
