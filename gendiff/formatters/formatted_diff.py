from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import convert_json


def formatted_diff(diff, formatter):
    if formatter == 'stylish':
        return stylish(diff)
    if formatter == 'plain':
        return plain(diff)
    if formatter == 'json':
        return convert_json(diff)
