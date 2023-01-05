#!/usr/bin/env python3
""" A type-annotation."""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the element length."""
    return [(i, len(i)) for i in lst]
