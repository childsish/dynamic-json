import unittest

from dynamic_json import load

class TestDynamicJson(unittest.TestCase):
    def test_load(self):
        fhndl = open('cfg.json')
        cfg = load(fhndl)
        fhndl.close()

        self.assertEquals(set(cfg), set(('project_name', 'dirs', 'exes', 'bases_per_chromosome')))
        self.assertEquals(cfg.project_name, 'hello-world')
        self.assertEquals(cfg.dirs.home, '/home/user')
        self.assertEquals(cfg.dirs.venv, '/home/user/venvs/hello-world')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
