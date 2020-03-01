[![Build Status](https://travis-ci.org/childsish/dynamic-json.svg?branch=master)](https://travis-ci.org/childsish/dynamic-json)

dynamic-json
============

Dynamic-json allows self-referential entries in a json file. It requires no dependencies, but lacks all the nice features of the yaml specification. If you prefer yaml then see [dynamic-yaml][dynamic-yaml].

Usage
-----

The key feature that was introduced is the ability for a string scalar to reference other parts of the configuration tree. This is done using the Python string formatting syntax. The characters '{' and '}' enclose a reference to another entry in the configuration structure. The reference takes the form key1.key2 where key1 maps to another mapping object and can be found in the root mapping, and key2 can be found in key1's mapping object. Multiple levels of nesting can be used (eg. key1.key2.key3 etc...).

An example yaml configuration:
```json
{
  "project_name": "hello-world",
  "dirs": {
    "home": "/home/user",
    "venv": "{dirs.home}/venvs/{project_name}",
    "data": "{dirs.venv}/data",
    "output": "{dirs.data}/output-{parameters.parameter1}-{parameters.parameter2}"
  },
  "parameters": {
    "parameter1": "a",
    "parameter2": "b"
  }
}
```

Reading in a json file:

```python
import dynamic_json

with open('/path/to/file.json') as fileobj:
    cfg = dynamic_json.load(fileobj)
    assert cfg.dirs.venv == '/home/user/venvs/hello-world'
    assert cfg.dirs.output == '/home/user/venvs/hello-world/data/output-a-b'
```

As the variables are dynamically resolved, it is also possible to combine this with `argparse`:

```python
import dynamic_json

from argparse import ArgumentParser

with open('/path/to/file.yaml') as fileobj:
    cfg = dynamic_json.load(fileobj)
    parser = ArgumentParser()
    parser.add_argument('--parameter1')
    parser.add_argument('--parameter2')
    parser.parse_args('--parameter1 c --parameter2 d'.split(), namespace=cfg.parameters)
    assert cfg.dirs.output == '/home/user/venvs/hello-world/data/output-c-d'
```

Installation
------------

To install, simply run:

```bash
pip install dynamic-json
```

Restrictions
------------

Due to the short amount of time I was willing to spend on working upon this, there are a few restrictions that I could not overcome.

* **Certain keys can only be used via `__getitem__` and not `__getattr__`.**
Because `dict` comes with it's own set of attributes that are always resolved first, the values for the following keys must be gotten using the item getter rather than the attribute getter (eg. config['items'] vs. config.items):
  * append
  * extend
  * insert
  * remove
  * pop
  * clear
  * index
  * count
  * sort
  * reverse
  * copy 