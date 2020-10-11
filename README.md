
# jflat [![Travis](https://travis-ci.com/aosingh/json-flattener.svg?branch=main)](https://travis-ci.org/aosingh/json-flattener)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)]((https://www.python.org/downloads/release/python-370/)) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![PyPy3](https://img.shields.io/badge/python-PyPy3-blue.svg)](https://www.pypy.org/index.html)

Python utility to flatten a JSON object

## Install

```bash
mkdir jflat_test

cd jflat_test

virtualenv .venv --python=python3 

source .venv/bin/activate

pip install git+https://github.com/aosingh/json-flattener.git
```

### Dependencies

Dependencies are defined as install requirements in `setup.py`. You need not install them separately.
We use the following external libraries.

- click
    - To create a Command Line Interface (CLI) for `jflat`
- pytest
    - To run unit tests


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

Often it is convenient to test with an inline JSON string. Make sure you enclose the 
JSON string in single quotes as shown below

```bash
jflat '{"username":"xyz","password":{"hash": "e8c400f94e807f0d374d9c971bec018"}}'

```

The following output will be written to stdout.

```json5
{
  "password.hash": "e8c400f94e807f0d374d9c971bec018",
  "username": "xyz"
}
```

### File input 

Additionally, `jflat` can accept input from a file. 
Let's say our input file `input.json` looks like below

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
You will see the flattened JSON object printed to stdout

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

### Save the output to a file

The default behavior is to write the flattened JSON object to stdout. If you want to save the flattened JSON object to a file, you can use the `--out-file` option. An example
is shown below

```bash5
jflat < input.json --sort-keys --out-file=output.json
```

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

## Continuous Integration (CI)

The code repository is integrated with Travis CI. Current build matrix is shown below.

```yaml
language: python
matrix:
  include:
    - os: linux
      python: 3.6
    - os: linux
      python: 3.7
    - os: linux
      python: 3.8
    - os: linux
      python: pypy3
```

## Unit Test & Coverage

Unit tests are integrated with the build process. We use `coverage` to run the test cases and generate a coverage report.


```bash
coverage run -m pytest --verbose
```

```bash
coverage report -i -m

Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
jflat/__init__.py               1      0   100%
jflat/cli.py                   28      1    96%   38
jflat/flattener.py             25      0   100%
jflat/tests/__init__.py         0      0   100%
jflat/tests/test_jflat.py      98      0   100%
---------------------------------------------------------
TOTAL                         152      1    99%

```

## API

The Python API can be used to access the flattened Python dictionary directly. 

```python
from jflat.flattener import JSONFlattener

data = {
        "friends": {
            "1": {
                "name": "Mr. X",
                "age": 13,
                "hobbies":{
                    "football": True,
                    "vedic maths": False,
                    "origami": True
                }
            },
            "2": {
                "name": "Mr. Y",
                "age": 56,
                "hobbies": {
                    "football": False,
                    "vedic maths": True,
                    "origami": False
                }
            }
        }
    }

j = JSONFlattener(data=data)
flattened_dict = j()

print(flattened_dict)

>>> {'friends.1.age': 13,
     'friends.1.hobbies.football': True,
     'friends.1.hobbies.origami': True,
     'friends.1.hobbies.vedic maths': False,
     'friends.1.name': 'Mr. X',
     'friends.2.age': 56,
     'friends.2.hobbies.football': False,
     'friends.2.hobbies.origami': False,
     'friends.2.hobbies.vedic maths': True,
     'friends.2.name': 'Mr. Y'}         

```


## Notes

- Standard python library `json` is used to parse the input JSON object and also
serialize the flattened dict.

- Iterative Depth First Search (DFS) is used to flatten the JSON object.
 
- The following JSON types are tested.
    - number
    - true
    - false
    - null
    - object
    
- In the current implementation, if the JSON object has an array, the array will be skipped.

- The name `jflat` is inspired from command-line JSON processor `jq`. 


## TODO

- Determine the maximum level of nesting supported.


