#!/usr/bin/env python3
""" Writing strings to Redis"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functool import wraps


def count_calls(method: Callable) -> Callable:
    """Count methods calls decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Call history  methods decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        output = method(self, *args, **kwargs)
        method_name = method.__qualname__
        self._redis.rpush(f"{method_name}:inputs", str(args))
        self._redis.rpush(f"{method_name}:outputs", str(output))
        return output
    return wrapper


def replay(method: Callable) -> Callable:
    """methods replay decorator"""
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode("utf-8")
    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)
    print(f"{method_name} was called {count} times:")
    for i, o in zip(inputs, outputs):
        print(f"{method_name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache(object):
    """
        Cache class
    """
    def __init__(self):
        """initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            generate random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @staticmethod
    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Function that return a value"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    @staticmethod
    def get_str(self, value: bytes) -> str:
        """to get string"""
        return str(value)

    def get_int(self, value: bytes) -> int:
        """to get integer"""
        return int(value)
