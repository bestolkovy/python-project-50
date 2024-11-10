from gendiff.formatters.stylish import stylish, plain


def formatted_diff(diff, formatter):
    if formatter == 'stylish':
        return stylish(diff)
    if formatter == 'plain':
        return plain(diff)
