def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value == 'false' or value == 'true' or value == 'null':
        return value
    else:
        return f"'{value}'"


def format_data(data, father_key=''):
    result = []
    for item in data:
        status = item.get('status')
        key = item.get('key')
        full_key = f'{father_key}.{key}' if father_key else key
        if status == 'added':
            value = item.get('value')
            f_v = format_value(value)
            result.append(f"Property '{full_key}' was added with value: {f_v}")
        elif status == 'deleted':
            result.append(f"Property '{full_key}' was removed")
        elif status == 'changed':
            value_old = format_value(item['value_old'])
            value_new = format_value(item['value_new'])
            result.append(f"Property '{full_key}' was updated. From {value_old} to {value_new}")  # noqa: E501
        elif status == 'nested':
            nested_changes = item.get('value')
            result.extend(format_data(nested_changes, full_key))
    return result


def plain(formated_data):
    return '\n'.join(format_data(formated_data))
