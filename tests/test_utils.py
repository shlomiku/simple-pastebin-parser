import unittest

from simple_pastebin_parser.utils import InvalidPastebinUrl, Url, PASTEBIN_URL_PREFIX


class TestUrl(unittest.TestCase):
    def test_invalid_url(self):
        try:
            Url("shlomi")
        except InvalidPastebinUrl:
            pass

    def test_valid_url(self):
        url = Url(PASTEBIN_URL_PREFIX + "shlomi")
        self.assertEqual(str(url), PASTEBIN_URL_PREFIX + "shlomi")


if __name__ == '__main__':
    unittest.main()
