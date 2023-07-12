#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """ Async Comprehensions. """
    return [i async for i in async_generator()]
