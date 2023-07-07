#!/usr/bin/env python3
"""
Module that takes a dict and a key and returns the value, None if missing.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Method that takes a dict and a key and returns the value,
    None if missing.
    """
    if key in dct:
        return dct[key]
    else:
        return default
