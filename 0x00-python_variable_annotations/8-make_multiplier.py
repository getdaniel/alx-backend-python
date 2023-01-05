#!/usr/bin/env python3
from typing import Callable
"""A type-annotation of make_multiplier."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return multiplies a float by multiplier."""
    return lambda x: x * multiplier
