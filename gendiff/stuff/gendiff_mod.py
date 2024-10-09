def format_data(data):
    result = '{\n'
    
    for item in data:
        status = item['status']
        key = item['key']
        depth = item['depth']
        indent = '    ' * depth

        # Проверяем, есть ли ключ 'value' в элементcccе
        value = item.get('value', None)
        
        if status == 'nested' and isinstance(value, list):
            result += f'{indent}  {key}: {format_data(value)}'
        else:
            if status == 'added':
                result += f'{indent}+ {key}: {format_value(value, depth)}\n'
            elif status == 'deleted':
                result += f'{indent}- {key}: {format_value(value, depth)}\n'
            elif status == 'changed':
                result += f'{indent}- {key}: {format_value(item["value_old"], depth)}\n'
                result += f'{indent}+ {key}: {format_value(item["value_new"], depth)}\n'
            else:
                result += f'{indent}  {key}: {format_value(value, depth)}\n'
    
    result += '    ' * (depth - 1) + '}\n'
    return result


def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        formatted = '{\n'
        for k, v in value.items():
            formatted += f'{indent}    {k}: {v}\n'
        formatted += indent + '}'
        return formatted
    elif isinstance(value, list):
        return format_data(value)
    else:
        return str(value)
