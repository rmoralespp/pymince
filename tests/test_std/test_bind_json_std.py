import io
import json
import sys
import unittest.mock

import pytest

import pymince.std


@pytest.fixture()
def stub_stdin_payload():
    sys_stdin = sys.stdin
    initial = {"in": "value"}
    sys.stdin = io.TextIOWrapper(buffer=io.BytesIO(json.dumps(initial).encode()))
    try:
        yield initial
    finally:
        sys.stdin = sys_stdin


def test_bind_json_std_with_output(capsys, stub_stdin_payload):
    expected = {"output": "value"}
    function = unittest.mock.Mock(return_value=expected)
    pymince.std.bind_json_std()(function)()
    captured = capsys.readouterr()
    function.assert_called_once_with(data=stub_stdin_payload)
    assert captured.out == json.dumps(expected)


def test_bind_json_std_without_output(capsys, stub_stdin_payload):
    function = unittest.mock.Mock(return_value=None)
    pymince.std.bind_json_std()(function)()
    captured = capsys.readouterr()
    function.assert_called_once_with(data=stub_stdin_payload)
    assert captured.out == ""
