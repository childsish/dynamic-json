dynamic-json
============

Dynamic-json allows entries in a json file to refer to each other. It requires no dependencies, but lacks all the nice features of the yaml specification. If you prefer yaml then see [dynamic-yaml][dynamic-yaml].

Usage
-----

Json files are written as they normally are. However, it's now possible to include references to other entries in the json file. An example json file could look like:

```json
{
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
    }
}
```

Reading in a json file:

```python
import dynamic_json

fileobj = open()
cfg = dynamic_json.load(fileobj)
fileobj.close()
```

Now, the entry `cfg.dirs.venv` will resolve to `"/home/user/venvs/hello-world"`.

Installation
------------

To install, simply run:

```bash
pip install git+https://github.com/childsish/dynamic-json
```

[dynamic-yaml]: https://github.com/childsish/dynamic-yaml
