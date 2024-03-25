#!/usr/bin/env python3
"""task 14"""


def top_students(mongo_collection):
    """ function that returns all
    students sorted by average score"""
    pipline = [
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ]
    return mongo_collection.aggregate(pipline).sort("averageScore", -1)
