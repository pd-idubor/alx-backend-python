#!/usr/bin/env python3
"""Async Basics"""

import asyncio
import random
from typing import List

# wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay and returns it"""
    res = await asyncio.gather(*(task_wait_random(max_delay)
                                 for x in range(n)))
    return sorted(res)
