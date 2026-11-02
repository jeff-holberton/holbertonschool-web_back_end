#!/usr/bin/env python3
"""tasks module"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a task"""

    return wait_random(max_delay)
