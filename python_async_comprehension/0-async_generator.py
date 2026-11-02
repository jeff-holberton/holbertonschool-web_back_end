#!/usr/bin/env python3
"""async generator that yields a random number per iteration"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generator that yields a random number per iteration"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
