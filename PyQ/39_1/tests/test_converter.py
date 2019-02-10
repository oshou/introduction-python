import unittest
from converter import list_to_dict


class TestListToDict(unittest.TestCase):
    def test_default_key(self):
        actual = list_to_dict(
            [{'id': 1, 'name': 'ロッシ'},
             {'id': 2, 'name': 'マルケス'},
             {'id': 3, 'name': 'ロレンソ'}],
        )
        expected = {
            1: {'id': 1, 'name': 'ロッシ'},
            2: {'id': 2, 'name': 'マルケス'},
            3: {'id': 3, 'name': 'ロレンソ'},
        }
        self.assertEqual(actual, expected)

    def test_with_key(self):
        actual = list_to_dict(
            [{'code': 'Val', 'name': 'ロッシ'},
             {'code': 'Mar', 'name': 'マルケス'},
             {'code': 'Lor', 'name': 'ロレンソ'}],
            key='code'
        )
        expected = {
            'Val': {'code': 'Val', 'name': 'ロッシ'},
            'Mar': {'code': 'Mar', 'name': 'マルケス'},
            'Lor': {'code': 'Lor', 'name': 'ロレンソ'},
        }
        self.assertEqual(actual, expected)

    def test_duplicate_key(self):
        actual = list_to_dict(
            [{'code': 'Val', 'name': 'ロッシ'},
             {'code': 'Val', 'name': 'マルケス'}],
            key='code'
        )
        expected = {
            'Val': {'code': 'Val', 'name': 'マルケス'},
        }
        self.assertEqual(actual, expected)
