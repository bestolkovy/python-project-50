from gendiff import generate_diff, parsing
import json


def test_compare():
    file1 = json.load(open('./tests/fixtures/file1.json'))
    file2 = json.load(open('./tests/fixtures/file2.json'))
    assert generate_diff(file1, file2) == open('./tests/fixtures/test1.txt').read() # noqa


def test_parsing():
    assert parsing('./tests/fixtures/file1.json') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False} # noqa
    assert parsing('./tests/fixtures/file2.yml') == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'} # noqa
