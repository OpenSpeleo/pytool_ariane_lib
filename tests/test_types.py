#!/usr/bin/env python

import unittest

from ariane_lib.types import UnitType
from ariane_lib.types import ArianeFileType
from ariane_lib.types import ProfileType
from ariane_lib.types import ShotType


class EnumTypesTest(unittest.TestCase):

    def test_invalid_unitType(self):
        with self.assertRaises(ValueError):
            _ = UnitType.from_str("lightyear")

    def test_invalid_fileType(self):
        with self.assertRaises(ValueError):
            _ = ArianeFileType.from_str("toml")

    def test_invalid_profileType(self):
        with self.assertRaises(ValueError):
            _ = ProfileType.from_str("diagonal")

    def test_invalid_shotType(self):
        with self.assertRaises(ValueError):
            _ = ShotType.from_str("hypothetical")


if __name__ == "__main__":
    unittest.main()