#!/usr/bin/env python3
"""
Module that takes a list of strings and returns a list of tuples containing
the string and its length.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
