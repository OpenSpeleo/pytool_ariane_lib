#!/usr/bin/env python

import json
import unittest

from pathlib import Path

from ariane_lib.parser import ArianeParser
from ariane_lib.types import ArianeFileType
from parameterized import parameterized_class

@parameterized_class(
    ('filepath'),
    [
        ("tests/artifacts/test_simple.tml",),
        ("tests/artifacts/test_simple.tmlu",),
        ("tests/artifacts/test_with_walls.tml",),
        ("tests/artifacts/test_large.tml",)
    ]
)
class ReadArianeFileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._file = Path(cls.filepath)
        if not cls._file.exists():
            raise FileNotFoundError(f"File not found: `{cls._file}`")

    def setUp(self) -> None:
        self._data = ArianeParser(self._file)

    def test_type(self):
        if self._data is None:
            raise ValueError("the Ariane file has not been read.")

        extension = self._file.suffix
        filetype = None
        if extension == ".tml":
            filetype = ArianeFileType.TML
        elif extension == ".tmlu":
            filetype = ArianeFileType.TMLU
        else:
            raise ValueError(f"Unexpected extension: {extension}")

        self.assertEqual(filetype, self._data.type)


if __name__ == '__main__':
    unittest.main()
