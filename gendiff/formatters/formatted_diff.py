from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import convert_json


def formatted_diff(diff, formatter):
    if formatter == 'stylish':
        return stylish(diff)
    if formatter == 'plain':
        return plain(diff)
    if formatter == 'json':
        return convert_json(diff)
