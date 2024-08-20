from gendiff import parsing


# эту хуету в форматтеры отправить
def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def stylish_formatter(dict):
