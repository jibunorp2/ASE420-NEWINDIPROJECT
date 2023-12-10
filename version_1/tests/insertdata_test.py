import unittest
from datetime import date

from src import backend
from src.backend import insertdata, view, drop_table


class TestInsertData(unittest.TestCase):

    def setUp(self):
        # Set up the test by creating a temporary database and inserting sample data
        drop_table()  # Drop the existing table
        backend.create_table()
        insertdata(date(2023, 1, 1), "08:00", "12:00", "Task 1", "Tag 1")
        insertdata(date(2023, 1, 2), "09:00", "13:00", "Task 2", "Tag 2")

    # def tearDown(self):
    #     # Clean up after the test by dropping the temporary table
    #     drop_table()

    def test_insertdata(self):
        # Insert new data and check if the length is correct
        insertdata(date(2023, 1, 3), "10:00", "14:00", "Task 3", "Tag 3")

        # Retrieve the data and check the length
        result = view().fetchall()
        self.assertEqual(len(result), 3)  # Expecting 3 rows after the insertion


if __name__ == '__main__':
    unittest.main()
