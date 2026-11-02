#!usr/bin/env python3
"""basic async syntax"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> int:
    """wait_random function: generates a random number
    between 0 and max_delay, waits the amount generated
    and returns the wait time"""

    wait_value = random.uniform(0, max_delay)
    await asyncio.sleep(wait_value)
    return wait_value
