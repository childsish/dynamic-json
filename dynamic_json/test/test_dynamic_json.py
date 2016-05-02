import unittest

from dynamic_json import load
from cStringIO import StringIO


class TestDynamicJson(unittest.TestCase):
    def test_load(self):
        fileobj = StringIO('''{
    "project_name": "hello-world",
    "dirs": {
        "home": "/home/user",
        "venv": "{dirs.home}/venvs/{project_name}",
        "bin": "{dirs.venv}/bin",
        "data": "{dirs.venv}/data",
        "errors": "{dirs.data}/errors",
        "sessions": "{dirs.data}/sessions",
        "databases": "{dirs.data}/databases"
    },
    "exes": {
        "main": "{dirs.bin}/main",
        "test": "{dirs.bin}/test"
    },
    "bases_per_chromosome": [
        30432563,
        19705359,
        23470805,
        18585042,
        26992728,
        154478,
        366924
    ]
}
''')
        cfg = load(fileobj)
        fileobj.close()

        self.assertEquals(set(cfg), {'project_name', 'dirs', 'exes', 'bases_per_chromosome'})
        self.assertEquals(cfg.project_name, 'hello-world')
        self.assertEquals(cfg.dirs.home, '/home/user')
        self.assertEquals(cfg.dirs.venv, '/home/user/venvs/hello-world')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())