#!/usr/bin/env python3
"""exercise.py"""

import redis
import uuid
from typing import Union


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None) -> Union[str, bytes, int, float]:
        """get"""
        if fn is None:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key) -> str:
        """get_str"""
        return self.get(key, str)

    def get_int(self, key) -> int:
        """get_int"""
        return self.get(key, int)
