#!/usr/bin/env python3
""" Async Generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yield a random number b/n 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
