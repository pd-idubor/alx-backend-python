#!/usr/bin/env python3
"""Duck type"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck type iterable"""
    return [(i, len(i)) for i in lst]
