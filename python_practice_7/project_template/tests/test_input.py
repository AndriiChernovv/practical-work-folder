
import unittest
import os
import pandas as pd

from app.io.input import read_from_file_builtin, read_from_file_pandas


class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        # Текстовий файл
        with open("test_file.txt", "w", encoding="utf-8") as f:
            f.write("Це тестовий файл.")

        # CSV-файл
        df = pd.DataFrame({
            "Name": ["Alice", "Bob"],
            "Age": [30, 25]
        })
        df.to_csv("test_file.csv", index=False)

    def tearDown(self):
        os.remove("test_file.txt")
        os.remove("test_file.csv")

    def test_read_from_file_builtin_content(self):
        content = read_from_file_builtin("test_file.txt")
        self.assertEqual(content, "Це тестовий файл.")

    def test_read_from_file_builtin_type(self):
        content = read_from_file_builtin("test_file.txt")
        self.assertIsInstance(content, str)

    def test_read_from_file_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin("no_such_file.txt")

    def test_read_from_file_pandas_head(self):
        content = read_from_file_pandas("test_file.csv")
        self.assertIn("Alice", content)
        self.assertIn("Bob", content)

    def test_read_from_file_pandas_type(self):
        content = read_from_file_pandas("test_file.csv")
        self.assertIsInstance(content, str)

    def test_read_from_file_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas("no_such_file.csv")


if __name__ == '__main__':
    unittest.main()
