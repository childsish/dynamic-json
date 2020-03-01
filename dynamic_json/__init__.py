import json


def load(infile):
    from .json_wrappers import JsonDict

    data = json.load(infile, object_pairs_hook=JsonDict)
    data.set_as_root()
    return data
