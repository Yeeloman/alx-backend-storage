#!/usr/bin/env python3
"""task 14"""


def top_students(mongo_collection):
    """ function that returns all
    students sorted by average score"""
    pipline = [
        {"$unwind": "$topics"},
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipline).sort("averageScore", -1)
