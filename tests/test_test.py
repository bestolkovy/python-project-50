from gendiff import format_data, diff_build, format_value, parsing
import json


def test_compare():
    file1 = json.load(open('./tests/fixtures/file1.json'))
    file2 = json.load(open('./tests/fixtures/file2.json'))
    diff = diff_build(file1, file2)
    assert format_data(diff) == open('./tests/fixtures/test1.txt').read() # noqa


def test_compare2():  # добавить yml
    nested1j = json.load(open('./tests/fixtures/nested1.json'))
    nested2j = json.load(open('./tests/fixtures/nested2.json'))
    diff = diff_build(nested1j, nested2j)
    assert format_data(diff) == open('./tests/fixtures/nested_test.txt').read() # noqa


def test_parsing():
    assert parsing('./tests/fixtures/file1.json') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False} # noqa
    assert parsing('./tests/fixtures/file2.yml') == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'} # noqa
