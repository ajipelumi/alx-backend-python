#!/usr/bin/env python3
"""
Module that takes a list and returns its first element, None if empty.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Method that takes a list and returns its first element, None if empty.
    """
    if lst:
        return lst[0]
    else:
        return None
