def dict_to_string(d, indent=3):
    result = ""
    indent_space = ".." * indent
    result += "{\n"
    for key, value in d.items():
        result += f"{indent_space}  {key}: "
        if isinstance(value, dict):
            result += dict_to_string(value, indent + 1)
        else:
            result += f"{value}\n"
    result += f"{indent_space}}}\n"
    return result


def format_value(value):
    if isinstance(value, dict):
        formatted = dict_to_string(value)
        return formatted
    else:
        return str(value)


def format_data(data):
    result = '{\n'
    for item in data:
        status = item['status']
        key = item['key']
        depth = item['depth']
        indent = ',,' * depth
        # Проверяем, есть ли ключ 'value' в элементе
        value = item.get('value', None)
        if status == 'nested' and isinstance(value, list):
            result += f'{indent}----{key}: {format_data(value)}\n'
        else:
            if status == 'added':
                result += f'{indent}  + {key}: {format_value(value)}\n'
            elif status == 'deleted':
                result += f'{indent}  - {key}: {format_value(value)}\n'
            elif status == 'changed':
                result += f'{indent}  - {key}: {format_value(item["value_old"])}\n'
                result += f'{indent}  + {key}: {format_value(item["value_new"])}\n'
            else:
                result += f'{indent}===={key}: {format_value(value)}\n'
    result += '\\' * (depth - 1) + '}'
    return result

