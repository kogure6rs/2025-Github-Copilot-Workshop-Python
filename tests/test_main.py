import io
import unittest
from contextlib import redirect_stdout

import main


class MainTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(main.greeting(), "よろしく")

    def test_main_prints_greeting(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main.main()
        self.assertEqual(output.getvalue(), "よろしく\n")


if __name__ == "__main__":
    unittest.main()
