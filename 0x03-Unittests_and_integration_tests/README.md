## Unittests and Integration Tests

This directory contains the code and resources for the Unittests and Integration Tests project.

**Unittests** are used to test individual units of code. This means that each unit of code is tested separately.

**Integration Tests** are used to test multiple units of code together. This means that multiple units of code are tested together.

### Topics Covered

- **Unittests**: We learn how to create unittests using the `unittest` module.

- **Unittests Mocking**: We learn how to use the `unittest.mock` module to mock objects.
Mocking is used to create fake objects to test our code.
This means that we can test our code without having to create the actual objects that our code depends on.

- **Parameterized Tests**: We learn how to use the `parameterized` module to create parameterized tests.
Parameterized tests are used to test the same code with different parameters.
This means that we can test our code with different parameters without having to write the same code multiple times.

- **Integration Tests**: We learn how to create integration tests using `fixtures`.

### Code Snippets
*calculator.py*
```python
#!/usr/bin/env python3
""" Calculator Module """

def add(a, b):
    """ Add two numbers """
    return a + b
```

*main.py*
```python
#!/usr/bin/env python3
""" Mock a unit test """
import unittest
from unittest import mock
from calculator import add


class TestAdd(unittest.TestCase):
    """ Test the add method """

    @mock.patch('calculator.add')
    def test_add(self, mock_add):
        """ Test the add method """
        mock_add.return_value = 5
        self.assertEqual(add(2, 2), 5)


if __name__ == '__main__':
    unittest.main()
```
The above code snippet shows how to mock the `add` function in the `calculator` module.
The `@mock.patch('calculator.add')` decorator is used to mock the `add` function in the `calculator` module.
The `mock_add.return_value = 5` line is used to set the return value of the `add` function to `5`.
This means that when the `add` function is called, it will return `5`.
This is how we can test our code without having to create the actual objects that our code depends on.

### Resources

The following resources were used to learn about Unittests and Integration Tests:

- [Unittests](https://docs.python.org/3/library/unittest.html)
- [Unittests Mocking](https://docs.python.org/3/library/unittest.mock.html)
- [Parameterized Tests](https://pypi.org/project/parameterized/)
- [Integration Tests](https://docs.pytest.org/en/latest/fixture.html)