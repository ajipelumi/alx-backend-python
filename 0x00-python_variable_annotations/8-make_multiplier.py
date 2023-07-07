#!/usr/bin/env python3
"""
Module that takes a float multiplier and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier and returns a function that
    multiplies a float by multiplier.
    """
    def multiply(arg: float) -> float:
        return multiplier * arg

    return multiply
