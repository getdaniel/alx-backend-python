#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Returns result after a delay of 10."""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)

    return wait_time
