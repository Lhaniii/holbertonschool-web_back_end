#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write measure_runtime
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Func run in four time"""
    start = time.time()
    run4 = [async_comprehension() for i in range(4)]
    i = await asyncio.gather(*run4)
    end = time.time()
    return end - start
