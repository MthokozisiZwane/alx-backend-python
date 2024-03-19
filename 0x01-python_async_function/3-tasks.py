#!/usr/bin/env python3

"""
A module of the function that takes an integer max_delay
and returns a asyncio.Task.
"""

import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """
    Regular function that returns an asyncio.Task for
    wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
