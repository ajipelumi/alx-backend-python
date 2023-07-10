#!/usr/bin/env python3
""" Execute multiple coroutines at the same time with async """
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ Returns a list of all the delays """
    delays: List[float] = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
