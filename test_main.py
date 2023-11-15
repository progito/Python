import sys
import unittest
from io import StringIO
from unittest.mock import patch
from lab1 import main

class TestMain(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def assert_stdout(self, expected_output, func, *args):
        with self.subTest():
            func(*args)
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)

    def test_correct_output(self):
        test1 = ["John", "200000", "http://example.com"]
        test2 = ["Tom", "12000", "http://example.com"]
        test3 = ["Max", "-100", "http://example.com"]
        test4 = ["Lera", "458391", "http://example.com"]
        test5 = ["Kate", "10000000", "http://example.com"]

        with patch("builtins.input", side_effect=test1):
            self.assert_stdout("Ожидаемый вывод", main)
        with patch("builtins.input", side_effect=test2):
            self.assert_stdout("Ожидаемый вывод", main)
        with patch("builtins.input", side_effect=test3):
            self.assert_stdout("Ожидаемый вывод", main)
        with patch("builtins.input", side_effect=test4):
            self.assert_stdout("Ожидаемый вывод", main)
        with patch("builtins.input", side_effect=test5):
            self.assert_stdout("Ожидаемый вывод", main)

if __name__ == "__main__":
    unittest.main()
