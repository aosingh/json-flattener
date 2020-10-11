
# jflat [![Travis](https://travis-ci.org/aosingh/json-flattener.svg?branch=main)](https://travis-ci.org/aosingh/json-flattener)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)]((https://www.python.org/downloads/release/python-370/)) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![PyPy3](https://img.shields.io/badge/python-PyPy3-blue.svg)](https://www.pypy.org/index.html)

Python utility to flatten a JSON object

## Install

```bash
pip install git+https://github.com/aosingh/json-flattener.git
```

### Install Dependencies

These dependencies are defined as install requirements in the `setup.py` file.  
You need not install them separately

- click
- pytest



## CLI

```bash

Usage: jflat [OPTIONS] [JSON_STRING]

Options:

  --log-level [CRITICAL|FATAL|ERROR|WARN|WARNING|INFO|DEBUG|NOTSET]
  --out-file TEXT                 Path to the output JSON file
  --sort-keys / --no-sort-keys    [default: False]
  --help                          Show this message and exit.

```

## Test

To run unit test cases, use the `pytest` command

```bash
pytest --verbose
```

```text
collected 15 items                                                                                                                        

jflat/tests/test_jflat.py::test_empty_dict PASSED                                                                                   [  6%]
jflat/tests/test_jflat.py::test_plain_dict PASSED                                                                                   [ 13%]
jflat/tests/test_jflat.py::test_null_value PASSED                                                                                   [ 20%]
jflat/tests/test_jflat.py::test_bool_value PASSED                                                                                   [ 26%]
jflat/tests/test_jflat.py::test_unicode PASSED                                                                                      [ 33%]
jflat/tests/test_jflat.py::test_control_chars PASSED                                                                                [ 40%]
jflat/tests/test_jflat.py::test_quotes PASSED                                                                                       [ 46%]
jflat/tests/test_jflat.py::test_exponent PASSED                                                                                     [ 53%]
jflat/tests/test_jflat.py::test_skip_unknown_type PASSED                                                                            [ 60%]
jflat/tests/test_jflat.py::test_error_on_unknown_type PASSED                                                                        [ 66%]
jflat/tests/test_jflat.py::test_nesting PASSED                                                                                      [ 73%]
jflat/tests/test_jflat.py::test_cli PASSED                                                                                          [ 80%]
jflat/tests/test_jflat.py::test_cli_stdin PASSED                                                                                    [ 86%]
jflat/tests/test_jflat.py::test_cli_with_sort_keys PASSED                                                                           [ 93%]
jflat/tests/test_jflat.py::test_cli_output_file PASSED                                                                              [100%]

=========================================================== 15 passed in 0.04s ============================================================
```

## Examples
