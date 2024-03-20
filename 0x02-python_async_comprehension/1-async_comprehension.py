#!/usr/bin/env python3

"""
Collect 10 random numbers using an async comprehension
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Asynchronously collects 10 random numbers using async comprehension.
    Returns:
        List[int]: A list of 10 random integers between 0 and 10 (inclusive)

    """

    return [async_val async for async_val in async_generator()]
