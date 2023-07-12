## Python Async Comprehension

This directory contains the code and resources for the Python Async Comprehension project.

**Async Comprehensions** are used to create asynchronous comprehensions.
This means that the comprehension can be run in the background while the rest of the program continues to run.

### Topics Covered

- **Async Comprehensions**: We learn how to create asynchronous comprehensions.
This means that the comprehension can be run in the background while the rest of the program continues to run.

- **Await**: We learn how to use the `await` keyword to wait for an asynchronous comprehension to finish running.
This means that the program will wait for the asynchronous comprehension to finish running before continuing to run.

- **Async Libraries**: We learn how to use the `asyncio` library to create asynchronous comprehensions.

### Code Snippets

```python
#!/usr/bin/env python3
""" Async Comprehension """
import asyncio


async def async_generator() -> float:
    """ Async Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def async_comprehension() -> list[float]:
    """ Async Comprehension """
    return [i async for i in async_generator()]


print(asyncio.run(async_comprehension()))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Resources

The following resources were used to learn about Async Comprehensions:

- [Async Comprehensions](https://realpython.com/async-io-python/#async-comprehensions)
- [Await](https://realpython.com/async-io-python/#await)
- [Async Libraries](https://realpython.com/async-io-python/#async-libraries)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [PEP 530 -- Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [PEP 492 -- Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/)