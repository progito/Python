try:
    foo = "def main():"
    with open("lab1/main.py", "r") as file:
        code = file.read()
    if code.find(foo) <= -1:
        code_lines = code.split("\n")
        code_lines.append("")
        code_lines.insert(0, foo)
        temp = code_lines[0]
        code_lines[0] = code_lines[1]
        code_lines[1] = temp
        index = code_lines.index("def main():")
        for i in range(index + 1, len(code_lines)):
            code_lines[i] = f"    {code_lines[i]}"
        new_code = "\n".join(code_lines)
        with open("lab1/main.py", "w") as file:
            file.write(new_code)
    import unittest
    from unittest.mock import patch
    from io import StringIO
    from lab1 import main
except Exception as err:
    print(err)


class TestSimpleFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "10000", "https://"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_not_enough_followers(self, mock_stdout, mock_input):
        main.main()
        expected_output = "Привет John\nУ вас пока недостаточно подписчиков для кнопки Ютуба\nПодписаться на канал John вот ссылка https://"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["John", "100000", "https://"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_enough_followers(self, mock_stdout, mock_input):
        main.main()
        expected_output = "Привет John\nУ вас уже есть серебрянная кнопка\nПодписаться на канал John вот ссылка https://"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["John", "1000000", "https://"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_high_followers(self, mock_stdout, mock_input):
        main.main()
        expected_output = "Привет John\nУ вас уже есть серебрянная и золотая кнопки\nПодписаться на канал John вот ссылка https://"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == "__main__":


    unittest.main()
