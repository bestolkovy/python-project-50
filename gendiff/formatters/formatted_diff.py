from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def formatted_diff(diff, formatter):
    if formatter == 'stylish':
        return stylish(diff)
    if formatter == 'plain':
        return plain(diff)
