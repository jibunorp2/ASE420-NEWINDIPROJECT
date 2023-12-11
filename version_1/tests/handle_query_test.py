import sys
import unittest
from datetime import date
from io import StringIO

from src import main, backend
from src.backend import insertdata, drop_table


class TestInsertData(unittest.TestCase):

    def setUp(self):
        drop_table()
        backend.create_table()
        insertdata(date(2023, 1, 1), "08:00", "12:00", "Task 1", ":STUDY")
        insertdata(date(2023, 1, 2), "09:00", "13:00", "Task 2", ":STUDY")

    def test_query(self):
        sys.argv = ['proto_main.py', 'query', ':STUDY']

        captured_output = StringIO()
        sys.stdout = captured_output

        main.handle_query(':STUDY')

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertIn('(1, \'2023-01-01\', \'08:00\', \'12:00\', \'Task 1\', \':STUDY\')', output)

        pass


if __name__ == '__main__':
    unittest.main()
