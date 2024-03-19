#!/usr/bin/env python3

"""
A module that execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
from random import randint
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times concurrently with the specified max_delay.
    Returns a list of delays in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
