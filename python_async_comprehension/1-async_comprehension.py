#!/usr/bin/env python3
"""async generator that yields a random number per iteration"""

import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async comprehension that returns a list generated
    by the async generator"""

    return [n async for n in async_generator()]
