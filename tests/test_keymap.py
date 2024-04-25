#!/usr/bin/env python

import unittest

from ariane_lib.parser import ArianeParser
from ariane_lib.shot import SurveyShot
from ariane_lib.key_map import KeyMapMeta


class KeyMapTest(unittest.TestCase):

    def test_invalid_key(self):
        a = {}
        with self.assertRaises(ValueError):
            _ = ArianeParser._KEY_MAP.fetch(a, "CHUCK NORRIS")
        with self.assertRaises(ValueError):
            _ = SurveyShot._KEY_MAP.fetch(a, "CHUCK NORRIS")

    def test_missing_key(self):
        data = {}
        with self.assertRaises(KeyError):
            _ = ArianeParser._KEY_MAP.fetch(data, "name")
        with self.assertRaises(KeyError):
            _ = SurveyShot._KEY_MAP.fetch(data, "id")

    def _test_valid_key(self, data):
        self.assertTrue(ArianeParser._KEY_MAP.fetch(data, "_shots"))
        self.assertTrue(SurveyShot._KEY_MAP.fetch(data, "depthin"))

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
        self.assertIsNone(ArianeParser._KEY_MAP.fetch({}, "geoCoding"))
        self.assertTrue(ArianeParser._KEY_MAP.fetch(data, "geoCoding"))

    def test_invalid_class_creation(self):
        with self.assertRaises(AttributeError):
            class ImproperCls(metaclass=KeyMapMeta):
                pass


if __name__ == "__main__":
    unittest.main()