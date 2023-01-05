#!/usr/bin/python3
from typing import Iterable, List, Tuple, Sequence
""" A type-annotation."""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the element length."""
    return [(i, len(i)) for i in lst]
