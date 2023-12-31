#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').\
                                 async_comprehension


async def measure_runtime() -> float:
    """Run time measurement for four parallel comprehensions"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    runtime = time.perf_counter() - start
    return runtime
