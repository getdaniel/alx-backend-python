#!/usr/bin/env python3
from typing import List, Union
"""A type-annotation of sum_mixed_list."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of lists."""
    return float(sum(mxd_lst))
