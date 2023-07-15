#!/usr/bin/env python3
"""Duck typing"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type annotation"""
    if lst:
        return lst[0]
    else:
        return None
