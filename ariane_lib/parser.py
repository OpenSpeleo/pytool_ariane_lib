#!/usr/bin/env python

import os
import xmltodict
import json

from pathlib import Path
from zipfile import ZipFile

from ariane_lib.types import ArianeFileType


def _extract_zip(input_zip):
    input_zip=ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


class ArianeParser(object):

    def __init__(self, filepath: str, debug : bool = False) -> None:

        filepath = Path(filepath)
        if not filepath.is_file():
            raise FileNotFoundError(f"File not found: {filepath}")

        self._xml_data = None
        self._filetype = None
        if filepath.suffix == ".tml":
            self._filetype = ArianeFileType.TML
            self._xml_data = _extract_zip(filepath)["Data.xml"]

        elif filepath.suffix == ".tmlu":
            self._filetype = ArianeFileType.TMLU
            with open(filepath, "r") as f:
                self._xml_data = f.read()

        else:
            raise RuntimeError(f"Unknown file format: {filepath.suffix}")

        self._data = xmltodict.parse(self._xml_data)

    @property
    def type(self):
        return self._filetype
