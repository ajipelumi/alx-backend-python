#!/usr/bin/env python3
"""
Module that takes a list input_list of floats and integers and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and integers.
    """
    return sum(mxd_lst)
