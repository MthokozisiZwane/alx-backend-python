#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that yields random numbers asynchronously.
    And takes no arguments
    Yields:
        int: A random integer between 0 and 10

    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
