import unittest
from unittest.mock import patch
from datetime import datetime
from src import backend


class TestPriorityFeature(unittest.TestCase):

    def setUp(self):
        backend.create_table()

    def tearDown(self):
        backend.drop_table()

    def assertResultAlmostEqual(self, result, expected_result):
        # Helper function to assert that results are almost equal (rounded to the nearest tenth)
        self.assertEqual(len(result), len(expected_result))
        for r, er in zip(result, expected_result):
            self.assertAlmostEqual(r[1], er[1], places=1)  # Round to the nearest tenth

    def test_priority_query(self):
        # Insert test data
        backend.insertdata("2023-01-01", "10:00", "12:00", "Task1", "Tag1")
        backend.insertdata("2023-01-01", "14:00", "16:00", "Task2", "Tag2")
        backend.insertdata("2023-01-01", "09:00", "11:00", "Task1", "Tag3")

        # Mock current date and time to ensure consistent results
        with patch('backend.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 1, 1, 18, 0)  # Set the current date and time

            # Perform the priority query
            result = backend.query_top_3_priority()

        # Assert the result matches the expected outcome with rounding
        self.assertResultAlmostEqual(result, [('Task2', 2.0, 0), ('Task1', 2.0, 0)])


if __name__ == '__main__':
    unittest.main()
