#!/usr/bin/python3
from typing import Union, Tuple
"""A type annotation of to_kv."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returna a tuple."""
    return (k, v**2)
