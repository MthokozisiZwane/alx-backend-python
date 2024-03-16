#!/usr/bin/env python3

"""string and int/float to tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a string and an int/float to a tuple"""
    return (k, v * v)
