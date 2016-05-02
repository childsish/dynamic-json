import json

from json_wrappers import JsonDict, JsonList


def load(infile):
    data = json.load(infile, object_pairs_hook=JsonDict)
    data.set_as_root()
    return data
