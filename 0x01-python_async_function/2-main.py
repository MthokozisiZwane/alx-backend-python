#!/usr/bin/env python3

import asyncio
measure_time = __import__('2-measure_runtime').measure_time


async def main():
    n = 5
    max_delay = 9
    result = await measure_time(n, max_delay)
    print(result)

asyncio.run(main())
