import unittest
from unittest.mock import patch
from io import StringIO
from src import main


class TestHandleReport(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, start_date, end_date, expected_output, mock_stdout):
        main.handle_report(start_date, end_date)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_handle_report_valid_dates(self):
        expected_output = "('Sample Task', 'Sample Tag')"
        # Mocking the database functions for testing
        src.backend.query_by_date = lambda x: [("Sample Task", "Sample Tag")]
        self.assert_stdout("2023/01/01", "2023/01/01", expected_output)

    def test_handle_report_invalid_dates(self):
        expected_output = "Invalid date format. Please use the format YYYY/MM/DD."
        self.assert_stdout("invalid_date", "2023/01/01", expected_output)

    def test_handle_report_empty_result(self):
        expected_output = ""  # No output for an empty result
        src.backend.query_by_date = lambda x: []
        self.assert_stdout("2023/01/01", "2023/01/01", expected_output)

if __name__ == '__main__':
    unittest.main()