import json

from click.testing import CliRunner
from jflat.flattener import JSONFlattener
from jflat.cli import main


def test_empty_dict():
    f = JSONFlattener(data={})
    flattened_dict = f()
    assert flattened_dict == {}


def test_plain_dict():
    data = {
        'a': 1,
        'b': 2,
        'c': "test"
    }

    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_null_value():
    data = {
        'a': None
    }
    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_bool_value():
    data = {
        'a': True,
        'b': False,
    }
    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_unicode():
    data = {
        "e": "\ud83c\udf89\ud83c\udf8a\ud83c\udf87\ud83c\udf86\ud83c\udf08\ud83d\udca5\u2728\ud83d\udcab\ud83d\udc45\ud83d\udeb9\ud83d\udeba\ud83d\udc83\ud83d\ude4c\ud83c\udfc3\ud83d\udc6c"
    }
    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_control_chars():
    data = {
        "e": "This is a string with \n breaks \\ \t probably making it \r unreadable"
    }

    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_quotes():
    data = {
        "e": "\"This is a string with \n breaks \t probably making it \r unreadable\""
    }

    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_exponent():
    data = {
        "e": 1e+22,
        "f": 2e-22
    }

    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert flattened_dict == data


def test_skip_unknown_type():

    # Unknown type is Tuple.
    data = {
        "a": 1,
        "b": ("1", "2")
    }
    expected_flattened_dict = {"a": 1}
    f = JSONFlattener(data=data, skip_unknown=True)
    flattened_dict = f()
    assert flattened_dict == expected_flattened_dict


def test_error_on_unknown_type():
    # Unknown type is Tuple.
    import pytest
    data = {
        "a": 1,
        "b": ("1", "2")
    }

    f = JSONFlattener(data=data, skip_unknown=False)
    with pytest.raises(TypeError):
        f()


def test_nesting():
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

    expected_flattened_dict = {'friends.1.age': 13,
                               'friends.1.hobbies.football': True,
                               'friends.1.hobbies.origami': True,
                               'friends.1.hobbies.vedic maths': False,
                               'friends.1.name': 'Mr. X',
                               'friends.2.age': 56,
                               'friends.2.hobbies.football': False,
                               'friends.2.hobbies.origami': False,
                               'friends.2.hobbies.vedic maths': True,
                               'friends.2.name': 'Mr. Y'}

    f = JSONFlattener(data=data)
    flattened_dict = f()
    assert expected_flattened_dict == flattened_dict


def test_cli():
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

    expected_flattened_dict = {'friends.1.age': 13,
                               'friends.1.hobbies.football': True,
                               'friends.1.hobbies.origami': True,
                               'friends.1.hobbies.vedic maths': False,
                               'friends.1.name': 'Mr. X',
                               'friends.2.age': 56,
                               'friends.2.hobbies.football': False,
                               'friends.2.hobbies.origami': False,
                               'friends.2.hobbies.vedic maths': True,
                               'friends.2.name': 'Mr. Y'}

    runner = CliRunner()
    result = runner.invoke(main, [json.dumps(data)])
    assert not result.exception
    assert result.exit_code == 0
    assert json.loads(result.output) == expected_flattened_dict


def test_cli_stdin():
    data = {
        "friends": {
            "1": {
                "name": "Mr. X",
                "age": 13,
                "hobbies": {
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

    expected_flattened_dict = {'friends.1.age': 13,
                               'friends.1.hobbies.football': True,
                               'friends.1.hobbies.origami': True,
                               'friends.1.hobbies.vedic maths': False,
                               'friends.1.name': 'Mr. X',
                               'friends.2.age': 56,
                               'friends.2.hobbies.football': False,
                               'friends.2.hobbies.origami': False,
                               'friends.2.hobbies.vedic maths': True,
                               'friends.2.name': 'Mr. Y'}

    runner = CliRunner()
    result = runner.invoke(main, input=json.dumps(data))
    assert not result.exception
    assert result.exit_code == 0
    assert json.loads(result.output) == expected_flattened_dict


def test_cli_with_sort_keys():
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

    expected_flattened_dict = {'friends.1.age': 13,
                               'friends.1.hobbies.football': True,
                               'friends.1.hobbies.origami': True,
                               'friends.1.hobbies.vedic maths': False,
                               'friends.1.name': 'Mr. X',
                               'friends.2.age': 56,
                               'friends.2.hobbies.football': False,
                               'friends.2.hobbies.origami': False,
                               'friends.2.hobbies.vedic maths': True,
                               'friends.2.name': 'Mr. Y'}

    runner = CliRunner()
    result = runner.invoke(main, ['--sort-keys', json.dumps(data)])
    assert not result.exception
    assert result.exit_code == 0
    assert json.loads(result.output) == expected_flattened_dict


def test_cli_output_file():
    import os
    import tempfile

    data = {
        "friends": {
            "1": {
                "name": "Mr. X",
                "age": 13,
                "hobbies": {
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

    expected_flattened_dict = {'friends.1.age': 13,
                               'friends.1.hobbies.football': True,
                               'friends.1.hobbies.origami': True,
                               'friends.1.hobbies.vedic maths': False,
                               'friends.1.name': 'Mr. X',
                               'friends.2.age': 56,
                               'friends.2.hobbies.football': False,
                               'friends.2.hobbies.origami': False,
                               'friends.2.hobbies.vedic maths': True,
                               'friends.2.name': 'Mr. Y'}

    with tempfile.NamedTemporaryFile(suffix='.json') as f:
        runner = CliRunner()
        result = runner.invoke(main, ['--out-file', f.name, json.dumps(data)])
        assert os.path.exists(f.name)
        assert result.exit_code == 0
        assert not result.exception
        with open(f.name) as fp:
            assert expected_flattened_dict == json.load(fp)









