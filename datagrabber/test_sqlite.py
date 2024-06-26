import unittest
from db.sqliteHandler import SqliteHandler


class TestSqlite(unittest.TestCase):

    def test_connect_with_empty_string(self):
        obj = SqliteHandler()

        with self.assertRaises(ValueError):
            obj.connect("")


if __name__ == '__main__':
    unittest.main()