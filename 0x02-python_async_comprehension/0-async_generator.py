#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import List


async def async_generator():
    """Async Generator"""
    i = 0
    while i < 10:
        yield random.uniform(0, 10)
        i += 1
        await asyncio.sleep(1)
