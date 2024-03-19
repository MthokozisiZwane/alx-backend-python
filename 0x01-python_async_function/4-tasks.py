#!/usr/bin/env python3

import asyncio
from typing import List, Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times concurrently with
    the specified max_delay.
    Returns a list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
