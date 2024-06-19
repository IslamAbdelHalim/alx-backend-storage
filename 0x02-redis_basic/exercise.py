#!/usr/bin/env python3
""" Writing strings to Redis"""

import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache(object):
    """
        Cache class
    """
    def __init__(self):
        """initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            generate random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Function that return a value"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, value: bytes) -> str:
        """to get string"""
        return str(value)

    def get_int(self, value: bytes) -> int:
        """to get integer"""
        return int(value)
