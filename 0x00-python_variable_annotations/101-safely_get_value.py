#!/usr/bin/python3
from typing import Any, Mapping, Union, TypeVar
"""A type-annotaion of get-value."""


T = TypeVar('T')
Ret = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Ret:
    """ Return a value from a dict using a given value."""
    if key in dct:
        return dct[key]
    else:
        return default
