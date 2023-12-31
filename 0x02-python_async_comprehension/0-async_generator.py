#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    i = 0
    while i < 10:
        yield random.uniform(0, 10)
        i += 1
        await asyncio.sleep(1)
