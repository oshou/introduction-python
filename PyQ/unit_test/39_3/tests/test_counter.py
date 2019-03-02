import tempfile
import unittest

from counter import count_file_lines


class TestCountFileLines(unittest.TestCase):
    def test_count(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""one
two
three
four
""")
            f.flush()
            actual = count_file_lines(f.name)
        self.assertEqual(actual, 4)
