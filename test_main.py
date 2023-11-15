try:
    foo = "def main():"
    with open("lab1_1/list.py", "r") as file:
        code = file.read()
    print(code.find(foo))
    if code.find(foo) <= -1:
        code_lines = code.split("\n")
        code_lines.append("")
        print(code_lines)
        code_lines.insert(0, foo)
        print(code_lines)

        index = code_lines.index("def main():")
        for i in range(index + 1, len(code_lines)):
            code_lines[i] = f"    {code_lines[i]}"
        new_code = "\n".join(code_lines)
        with open("lab1_1/list.py", "w") as file:
            file.write(new_code)
    import unittest
    from unittest.mock import patch
    from io import StringIO
    from lab1_1 import list
except Exception as err:
    print(err)


class TestSimpleFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_not_enough_followers(self, mock_stdout, mock_input):
        list.main()
        expected_output = "ошибка"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch("builtins.input", side_effect=["8", "3", "3", "1", "-1", "2", "4", "5", "-5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_enough_followers(self, mock_stdout, mock_input):
        list.main()
        expected_output = "[-5, -1, 1, 2, 3, 3, 4, 5]"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)



if __name__ == "__main__":


    unittest.main()
