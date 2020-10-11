
# jflat [![Travis](https://travis-ci.org/aosingh/json-flattener.svg?branch=main)](https://travis-ci.org/aosingh/json-flattener)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)]((https://www.python.org/downloads/release/python-370/)) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![PyPy3](https://img.shields.io/badge/python-PyPy3-blue.svg)](https://www.pypy.org/index.html)

Python utility to flatten a JSON object

## Install

```bash
pip install git+https://github.com/aosingh/json-flattener.git
```

### Dependencies

These dependencies are defined as install requirements in the `setup.py` file.  
You need not install them separately

- click
- pytest


## Unit Test

To run unit test cases, use the `pytest` command

```bash
pytest --verbose
```

```text
collected 15 items                                                                                                                        

jflat/tests/test_jflat.py ...............                                                                                           [100%]

=========================================================== 15 passed in 0.04s ============================================================
```

## CLI

```bash

Usage: jflat [OPTIONS] [JSON_STRING]

Options:

  --log-level [CRITICAL|FATAL|ERROR|WARN|WARNING|INFO|DEBUG|NOTSET]
  --out-file TEXT                 Path to the output JSON file
  --sort-keys / --no-sort-keys    [default: False]
  --help                          Show this message and exit.

```

## Examples

### Simple json string

```json5
jflat '{"username":"xyz","password":"xyz"}'

```

```json5
{
  "password": "xyz",
  "username": "xyz"
}
```

### File input 

```bash
jflat < /Users/as/jflat/jflat/tests/sample_files/nested.json
```

```json5
{
  "$c.e": "\ud83c\udf89\ud83c\udf8a\ud83c\udf87\ud83c\udf86\ud83c\udf08\ud83d\udca5\u2728\ud83d\udcab\ud83d\udc45\ud83d\udeb9\ud83d\udeba\ud83d\udc83\ud83d\ude4c\ud83c\udfc3\ud83d\udc6c",
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.11.32.23.45.56.76.": 10,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.11.32.23.45.56.65": "\"i am deeply nested\"",
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.kl": -122200000000000.0,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.lm": 10000000000.0,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.jk": null,
  "b": true,
  "a": 1
}
```

### Sort keys

```bash
jflat < /Users/as/jflat/jflat/tests/sample_files/nested.json --sort-keys
```

```json5
{
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.11.32.23.45.56.65": "\"i am deeply nested\"",
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.11.32.23.45.56.76.": 10,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.jk": null,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.kl": -122200000000000.0,
  "$c.d.e.f.k.l.m.n.k.l.f.1.2.3.4.5.6.7.8.9.10.lm": 10000000000.0,
  "$c.e": "\ud83c\udf89\ud83c\udf8a\ud83c\udf87\ud83c\udf86\ud83c\udf08\ud83d\udca5\u2728\ud83d\udcab\ud83d\udc45\ud83d\udeb9\ud83d\udeba\ud83d\udc83\ud83d\ude4c\ud83c\udfc3\ud83d\udc6c",
  "a": 1,
  "b": true
}

```

### Dump the output to a file

```bash5
jflat < /Users/as/jflat/jflat/tests/sample_files/nested.json --sort-keys --out-file=test.json
```

```text
2020-10-11 13:50:02,456 - Output file path test.json
```


