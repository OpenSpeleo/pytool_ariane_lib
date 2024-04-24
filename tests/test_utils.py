#!/usr/bin/env python

import unittest

from ariane_lib.parser import _KEY_MAP as PARSER_MAP
from ariane_lib.shot import _KEY_MAP as SHOT_MAP


class KeyMapTest(unittest.TestCase):

    def test_invalid_key(self):
        a = {}
        with self.assertRaises(KeyError):
            _ = PARSER_MAP.fetch(a, "CHUCK NORRIS")
        with self.assertRaises(KeyError):
            _ = SHOT_MAP.fetch(a, "CHUCK NORRIS")

    def test_missing_key(self):
        data = {}
        with self.assertRaises(KeyError):
            _ = PARSER_MAP.fetch(data, "name")
        with self.assertRaises(KeyError):
            _ = SHOT_MAP.fetch(data, "id")

    def _test_valid_key(self, data):
        self.assertTrue(PARSER_MAP.fetch(data, "_shots"))
        self.assertTrue(SHOT_MAP.fetch(data, "depthin"))

    def test_valid_key_tml(self):
        data = {
            "DepthIn": True,
            "SurveyData": True
        }
        self._test_valid_key(data)

    def test_valid_key_tmlu(self):
        data = {
            "DPI": True,
            "SRVD": True
        }
        self._test_valid_key(data)

    def test_optional_key(self):
        data = {
            "geoCoding": True
        }
        self.assertIsNone(PARSER_MAP.fetch({}, "geoCoding"))
        self.assertTrue(PARSER_MAP.fetch(data, "geoCoding"))


if __name__ == "__main__":
    unittest.main()