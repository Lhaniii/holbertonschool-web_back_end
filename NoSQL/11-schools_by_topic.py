#!/usr/bin/env python3
"""Write a Python function that returns the list of
school having a specific topic:"""


def schools_by_topic(mongo_collection, topic):
    """prototype used for specific school research"""
    query = {"topics": topic}
    schools = mongo_collection.find(query)
    return list(schools)
