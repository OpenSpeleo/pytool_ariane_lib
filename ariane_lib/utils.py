#!/usr/bin/env python

from collections import UserDict
from collections import UserList


class OptionalArgList(UserList):
    pass


class KeyMapCls(UserDict):
    def fetch(self, data, key):
        if key in self.keys():
            possible_keys = self[key]
            try:
                for tentative_key in self[key]:
                    try:
                        return data[tentative_key]
                    except KeyError:
                        continue
                else:
                    raise KeyError(f"Unable to find any of {self[key]}")
            except KeyError:
                if isinstance(possible_keys, OptionalArgList):
                    return None
                raise
        else:
            raise KeyError(f"The key `{key}` does not exists inside `data`")


def maybe_convert_str_type(value):

    if not isinstance(value, str):
        return value
    
    if value in ["true", "false"]:
        return value == "true"

    try:
        value = int(value)
    except (ValueError, TypeError):
        try:
            value = float(value)
        except (ValueError, TypeError):
            pass

    return value