#!/usr/bin/env python3
"""A type annotation of to_kv."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returna a tuple."""
    return (k, v**2)
