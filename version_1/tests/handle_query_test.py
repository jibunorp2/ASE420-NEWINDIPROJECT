import sys
import unittest
from datetime import date
from io import StringIO

from src import main, backend
from src.backend import insertdata, drop_table


class TestInsertData(unittest.TestCase):

    def setUp(self):
        # Set up the test by creating a temporary database and inserting sample data
        drop_table()  # Drop the existing table
        backend.create_table()
        insertdata(date(2023, 1, 1), "08:00", "12:00", "Task 1", ":STUDY")
        insertdata(date(2023, 1, 2), "09:00", "13:00", "Task 2", ":STUDY")

    # def tearDown(self):
    #     # Clean up after the test by dropping the temporary table
    #     drop_table()

    def test_query(self):
        sys.argv = ['proto_main.py', 'query', ':STUDY']

        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the handle_query method
        # file_temp.handle_query('Tag 1')
        main.handle_query(':STUDY')

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Retrieve the captured output
        output = captured_output.getvalue().strip()

        # Check if the output matches expectations
        self.assertIn('(1, \'2023-01-01\', \'08:00\', \'12:00\', \'Task 1\', \':STUDY\')', output)

        pass


if __name__ == '__main__':
    unittest.main()
