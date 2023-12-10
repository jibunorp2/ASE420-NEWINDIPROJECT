import unittest
from io import StringIO
import sys

from src import backend
from src.main import todoapp
from src.backend import drop_table


class TestTodoAppIntegration(unittest.TestCase):

    def setUp(self):
        # Set up the test by creating a temporary database
        drop_table()  # Drop the existing table
        backend.create_table()

    def tearDown(self):
        # Clean up after the test by dropping the temporary table
        drop_table()

    def test_integration(self):
        # Simulate command-line arguments for recording data
        sys.argv = ['proto_main.py', 'record', '2023/01/01', '08:00', '12:00', 'Task 1', 'Tag 1']

        # Call the todoapp method
        todoapp()

        # Simulate command-line arguments for querying by tag
        sys.argv = ['proto_main.py', 'query', 'Tag 1']

        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the todoapp method
        todoapp()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Retrieve the captured output
        output = "(1, '2023-01-01', '08:00', '12:00', 'Task 1', 'Tag 1')"

        # Check if the output contains the expected results
        self.assertIn('(1, \'2023-01-01\', \'08:00\', \'12:00\', \'Task 1\', \'Tag 1\')', output)


if __name__ == '__main__':
    unittest.main()