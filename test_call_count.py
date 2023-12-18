# File: test_call_count.py

import unittest
from unittest.mock import MagicMock

def my_function():
    # Function to be tested
    pass

class TestCallCount(unittest.TestCase):
    def test_call_count(self):
        # Create a mock object for the function
        mocked_function = MagicMock()

        # Replace the actual function with the mock
        with unittest.mock.patch('__main__.my_function', new=mocked_function):
            # Perform some actions that should call the function
            my_function()
            my_function()
            my_function()

            # Check if the function was called three times
            self.assertEqual(mocked_function.call_count, 3)

if __name__ == '__main__':
    unittest.main()
