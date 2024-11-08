from gendiff.formatters.stylish import stylish


def formatted_diff(diff, formatter):
    if formatter == 'stylish':
        return stylish(diff)
