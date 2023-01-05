#!/usr/bin/env python3
"""A type-annotation of make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return multiplies a float by multiplier."""
    return lambda x: x * multiplier
