import unittest
import os
from app.io.output import print_to_console, write_to_file
from io import StringIO
import sys


class TestOutputFunctions(unittest.TestCase):

    def test_print_to_console_output(self):
        # Перехоплення виводу в консоль
        captured_output = StringIO()
        sys.stdout = captured_output
        print_to_console("Привіт")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Привіт")

    def test_write_to_file_creates_file(self):
        path = "test_output.txt"
        text = "Тестовий запис"
        write_to_file(path, text)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_write_to_file_content(self):
        path = "test_output.txt"
        text = "Це ще один тест"
        write_to_file(path, text)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, text)
        os.remove(path)


if __name__ == '__main__':
    unittest.main()
