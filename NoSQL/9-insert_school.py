#!/usr/bin/env python3
""" inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """New doc in school"""
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
