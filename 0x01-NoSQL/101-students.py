#!/usr/bin/env python3
"""task 14"""


def top_students(mongo_collection):
    """ function that returns all
    students sorted by average score"""
    return mongo_collection.aggregate([
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
    ])
