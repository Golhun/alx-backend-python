#!/usr/bin/env python3
"""
This is a simple task to get used to async syntax
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''function that returns random delay time after that period has elasped'''
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
