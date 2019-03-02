import unittest
import os
import tempfile
from dircounter import count_files


class TestCountFiles(unittest.TestCase):
    def test_count(self):
        with tempfile.TemporaryDirectory() as dirpath:
            with open(os.path.join(dirpath, 'file1'), mode="w", encoding="utf-8") as f1, \
                    open(os.path.join(dirpath, 'file2'), mode="w", encoding="utf-8") as f2:
                f1.write("file1")
                f1.flush()
                f2.write("file2")
                f2.flush()
                actual = count_files(dirpath)
            self.assertEqual(actual, 2)
