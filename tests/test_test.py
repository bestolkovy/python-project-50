from gendiff import generate_diff
from gendiff import parsing


def test_compare():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    assert generate_diff(file1, file2) == open('./tests/fixtures/test1.txt').read() # noqa


def test_compare2():  # добавить yml
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j) == open('./tests/fixtures/stylish_test.txt').read() # noqa


def test_compare3():
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j, 'plain') == open('./tests/fixtures/plain_test.txt').read() # noqa


def test_compare4():
    nested1j = './tests/fixtures/nested1.json'
    nested2j = './tests/fixtures/nested2.json'
    assert generate_diff(nested1j, nested2j, 'json') == open('./tests/fixtures/jsonn.json').read() # noqa


def test_parsing():
    assert parsing('./tests/fixtures/file1.json') == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False} # noqa
    assert parsing('./tests/fixtures/file2.yml') == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'} # noqa
