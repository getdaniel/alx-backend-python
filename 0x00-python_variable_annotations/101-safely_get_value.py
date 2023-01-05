#!/usr/bin/env python3
"""A type-annotaion of get-value."""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Ret = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Ret:
    """ Return a value from a dict using a given value."""
    if key in dct:
        return dct[key]
    else:
        return default
