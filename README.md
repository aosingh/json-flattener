
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

Let's say our example `input.json` file looks like below

```json5
{
        "friends": {
            "1": {
                "name": "Mr. X",
                "age": 13,
                "hobbies": {
                    "football": true,
                    "vedic maths": false,
                    "origami": true
                }
            },
            "2": {
                "name": "Mr. Y",
                "age": 56,
                "hobbies": {
                    "football": false,
                    "vedic maths": true,
                    "origami": false
                }
            }
        }
}
```

Invoke the JSON flat command as shown below

```bash
jflat < input.json
```
```json5
{
  "friends.2.hobbies.origami": false,
  "friends.2.hobbies.vedic maths": true,
  "friends.2.hobbies.football": false,
  "friends.2.age": 56,
  "friends.2.name": "Mr. Y",
  "friends.1.hobbies.origami": true,
  "friends.1.hobbies.vedic maths": false,
  "friends.1.hobbies.football": true,
  "friends.1.age": 13,
  "friends.1.name": "Mr. X"
}
```

### Sort keys

Pass the `--sort-keys` flag to sort the keys alphabetically in the flattened JSON.

```bash
jflat < input.json --sort-keys
```
```json5
{
  "friends.1.age": 13,
  "friends.1.hobbies.football": true,
  "friends.1.hobbies.origami": true,
  "friends.1.hobbies.vedic maths": false,
  "friends.1.name": "Mr. X",
  "friends.2.age": 56,
  "friends.2.hobbies.football": false,
  "friends.2.hobbies.origami": false,
  "friends.2.hobbies.vedic maths": true,
  "friends.2.name": "Mr. Y"
}

```

### Output to a file

The default behavior is to write the flattened out to stdout. 

If you want to save the flattened JSON object to a file, you can use the `--out-file` option. An example
is shown below

```bash5
jflat < input.json --sort-keys --out-file=output.json
```

The log statement prints the path to the output file

```text
2020-10-11 13:50:02,456 - Output file is output.json
```

Verify the contents of the output file

```bash
cat output.json
```

```json5

{
  "friends.1.age": 13,
  "friends.1.hobbies.football": true,
  "friends.1.hobbies.origami": true,
  "friends.1.hobbies.vedic maths": false,
  "friends.1.name": "Mr. X",
  "friends.2.age": 56,
  "friends.2.hobbies.football": false,
  "friends.2.hobbies.origami": false,
  "friends.2.hobbies.vedic maths": true,
  "friends.2.name": "Mr. Y"
}
```


