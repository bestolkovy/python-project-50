# эту хуету в форматтеры отправить
def format_value1(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


# здесь у нас уже должен быть готовый дифф со всеми атрибутами эддед, ченджед.
def format_value(value, indent=1):
    """Formats value recursively if it's a dictionary, or just returns string."""
    if isinstance(value, dict):
        items = []
        for k, v in value.items():
            items.append(f'{"...." * indent}{k}: {format_value(v, indent + 1)}')
        return '{\n' + '\n'.join(items) + f'\n{"...." * (indent - 1)}}}'
    else:
        return str(value).lower() if isinstance(value, bool) else str(value)


def format_data(d, indent=1):
    formatted_lines = []
    for key, value in d.items():
        status = value['status']
        if status == 'unchanged':
            formatted_lines.append(f'{".." * indent}{key}: {format_value(value["value"], indent)}')
        elif status == 'deleted':
            formatted_lines.append(f'{"...." * (indent - 1)}- {key}: {format_value(value["value"], indent)}')
        elif status == 'added':
            formatted_lines.append(f'{"...." * (indent - 1)}+ {key}: {format_value(value["value"], indent)}')
        elif status == 'changed':
            formatted_lines.append(f'{"...." * (indent - 1)}- {key}: {format_value(value["value_old"], indent)}')
            formatted_lines.append(f'{"...." * (indent - 1)}+ {key}: {format_value(value["value_new"], indent)}')
        elif status == 'nested':
            formatted_lines.append(f'{"...." * indent}{key}: {{')
            formatted_lines.append(format_data(value['value'], indent + 1))
            formatted_lines.append(f'{"...." * indent}}}')
    return '\n'.join(formatted_lines)


#formatted_str = "{\n" + format_data(data, 1) + "\n}"
#print(formatted_str)

