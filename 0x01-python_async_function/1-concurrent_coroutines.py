#!/usr/bin/env python3
"""
This is a task on concurrent coroutines
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    # Concurrent function example
    delays: List[float] = []
    tasks = []

    for i in range(n):
        background_task = asyncio.create_task(wait_random(max_delay))
        background_task.add_done_callback(
            lambda fn: delays.append(fn.result()))
        tasks.append(background_task)

    for task in tasks:
        await task

    return delays
