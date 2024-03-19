#!/usr/bin/env python3

import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """
    Regular function that returns an asyncio.Task for
    wait_random with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
