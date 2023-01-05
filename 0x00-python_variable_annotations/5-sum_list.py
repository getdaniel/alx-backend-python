#!/usr/bin/env python3
""" A type-annotation of sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return sum of list."""
    return float(sum(input_list))
