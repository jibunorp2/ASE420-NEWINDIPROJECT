import unittest
from datetime import date

from src import backend
from src.backend import insertdata, view, drop_table


class TestInsertData(unittest.TestCase):

    def setUp(self):
        drop_table()
        backend.create_table()
        insertdata(date(2023, 1, 1), "08:00", "12:00", "Task 1", "Tag 1")
        insertdata(date(2023, 1, 2), "09:00", "13:00", "Task 2", "Tag 2")


    def test_insertdata(self):

        insertdata(date(2023, 1, 3), "10:00", "14:00", "Task 3", "Tag 3")


        result = view().fetchall()
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
