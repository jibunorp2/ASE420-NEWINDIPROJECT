import unittest
from io import StringIO
import sys

from src import backend
from src.main import todoapp
from src.backend import drop_table


class TestTodoAppIntegration(unittest.TestCase):

    def setUp(self):
        drop_table()
        backend.create_table()

    def tearDown(self):
        drop_table()

    def test_integration(self):

        sys.argv = ['proto_main.py', 'record', '2023/01/01', '08:00', '12:00', 'Task 1', 'Tag 1']
        todoapp()


        sys.argv = ['proto_main.py', 'query', 'Tag 1']


        captured_output = StringIO()
        sys.stdout = captured_output


        todoapp()


        sys.stdout = sys.__stdout__


        output = "(1, '2023-01-01', '08:00', '12:00', 'Task 1', 'Tag 1')"

 
        self.assertIn('(1, \'2023-01-01\', \'08:00\', \'12:00\', \'Task 1\', \'Tag 1\')', output)


if __name__ == '__main__':
    unittest.main()
