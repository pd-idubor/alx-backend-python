#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a multiplier function"""
    def func(n: float, multiplier=multiplier) -> float:
        return n * multiplier
    return (func)
