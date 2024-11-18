from gendiff import generate_diff
from gendiff import parsing
from gendiff import diff_build
from gendiff import format_value
import json


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'


def test_nested_diff():
    file1 = json.load(open('./tests/fixtures/nested1.json'))
    file2 = json.load(open('./tests/fixtures/nested2.json'))
    assert str(diff_build(file1, file2)) == open('./tests/fixtures/diff.txt').read() # noqa


def test_compare_simple():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    assert generate_diff(file1, file2) == open('./tests/fixtures/test1.txt').read() # noqa


def test_compare2_stylish():  # добавить yml
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j) == open('./tests/fixtures/stylish_test.txt').read() # noqa


def test_compare_plain():
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j, 'plain') == open('./tests/fixtures/plain_test.txt').read() # noqa


def test_compare_jsonq():
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j, 'json') == open('./tests/fixtures/jsonn.json').read() # noqa


def test_parsing():
    assert parsing('./tests/fixtures/file1.json') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False} # noqa
    assert parsing('./tests/fixtures/file2.yml') == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'} # noqa
