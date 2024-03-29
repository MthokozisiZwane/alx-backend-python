#!/usr/bin/env python3

"""
This module provides a function to measure the runtime
of the wait_n coroutine.
"""


import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: float = 10.0) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
