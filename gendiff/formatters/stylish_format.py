def dict_to_string(dictionary, depth):
    result = ""
    indent_space = "    " * (depth + 1)
    result += "{\n"
    for key, value in dictionary.items():
        result += f"{indent_space}    {key}: "
        if isinstance(value, dict):
            result += dict_to_string(value, depth + 1) + '\n'
        else:
            result += f"{value}\n"
    result += f"{indent_space}}}"
    return result


def format_value(value, depth):
    if isinstance(value, dict):
        return dict_to_string(value, depth)
    else:
        return str(value)


def stylish(data):
    result = '{\n'
    for item in data:
        status = item['status']
        key = item['key']
        depth = item['depth']
        indent = '    ' * depth
        value = item.get('value', None)
        if status == 'nested' and isinstance(value, list):
            result += f'{indent}    {key}: {stylish(value)}\n'
        else:
            if status == 'added':
                result += f'{indent}  + {key}: {format_value(value, depth)}\n'
            elif status == 'deleted':
                result += f'{indent}  - {key}: {format_value(value, depth)}\n'
            elif status == 'changed':
                result += f'{indent}  - {key}: '
                result += f'{format_value(item["value_old"], depth)}\n'
                result += f'{indent}  + {key}: '
                result += f'{format_value(item["value_new"], depth)}\n'
            else:
                result += f'{indent}    {key}: {format_value(value, depth)}\n'
    result += '    ' * (depth) + '}'
    return result
