#!/usr/bin/env python

import datetime
import json

from typing import Any

from ariane_lib.types import ShotType
from ariane_lib.types import ProfileType
from ariane_lib.utils import maybe_convert_str_type
from ariane_lib.utils import KeyMapCls


_KEY_MAP = KeyMapCls(
    {
        "azimut": ["Azimut", "AZ"],
        "closuretoid": ["ClosureToID", "CID"],
        "color": ["Color", "CL"],
        "comment": ["Comment", "CM"],
        "date": ["Date", "DT"],
        "depth": ["Depth", "DP"],
        "depthin": ["DepthIn", "DPI"],
        "down": ["Down", "D"],
        "excluded": ["Excluded", "EXC"],
        "explorer": ["Explorer", "EX"],
        "fromid": ["FromID", "FRID"],
        "id": ["ID"],
        "inclination": ["Inclination", "INC"],
        "latitude": ["Latitude", "LT"],
        "left": ["Left", "L"],
        "length": ["Length", "LG"],
        "locked": ["Locked", "LK"],
        "longitude": ["Longitude", "LGT"],
        "name": ["Name", "NM"],
        "profiletype": ["Profiletype", "PRTY"],
        "right": ["Right", "R"],
        "section": ["Section", "SC"],
        "shape": ["Shape", "SH"],
        "type": ["Type", "TY"],
        "up": ["Up", "U"],
    }
)


class SurveyShot(object):
    def __init__(self, data) -> None:
        self._data = data

    def __repr__(self) -> str:
        repr = f"[{self.__class__.__name__} {self.id:04d}]:"
        for key in _KEY_MAP.keys():
            repr += f"\n\t- {key}: {getattr(self, key)}"
        return repr

    def __getattribute__(self, name: str) -> Any:
        if name in _KEY_MAP.keys():
            value = _KEY_MAP.fetch(self.data, name)
            if name == "profiletype":
                return ProfileType.from_str(value)

            if name == "type":
                return ShotType.from_str(value)

            if name == "date":
                year, month, day = [int(v) for v in value.split("-")]
                return datetime.datetime(year=year, month=month, day=day)

            return maybe_convert_str_type(value)

        return super().__getattribute__(name)

    @property
    def data(self):
        return self._data

    def to_json(self):
        return json.dumps(self.data, indent=4, sort_keys=True)
