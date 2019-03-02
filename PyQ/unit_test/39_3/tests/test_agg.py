import tempfile
import unittest
from agg import parse_ltsv, agg_ltsv_file


class TestParseLTSV(unittest.TestCase):
    def test_parse(self):
        with tempfile.NamedTemporaryFile(mode="w") as f:
            f.write("""level:INFO\tmessage:msg1
level:INFO\tmessage:msg2
level:ERROR\tmessage:error
""")
            f.flush()
            actual = parse_ltsv(
                'level:INFO\tmessage:メッセージ\tcreated_at:14000000')
        self.assertEqual(actual, {
            'level': 'INFO',
            'message': 'メッセージ',
            'created_at': '14000000'
        })


class TestAggLTSVFile(unittest.TestCase):
    def test_aggregate(self):
        with tempfile.NamedTemporaryFile(mode="w") as f:
            f.write("""level:INFO\tmessage:msg1
level:INFO\tmessage:msg2
level:ERROR\tmessage:error
""")
            f.flush()
            actual = agg_ltsv_file(f.name, 'level')
        self.assertEqual(actual, {
            'INFO': 2,
            'ERROR': 1
        })
