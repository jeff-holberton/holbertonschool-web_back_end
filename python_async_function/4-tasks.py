#!/usr/bin/env python3
"""tasks module"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n function, calls task_wait_random n times
    and prints each wait value in ascending order"""

    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(coroutines):
        delays.append(await finished)
    return delays
