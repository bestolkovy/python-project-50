# здесь у нас уже должен быть готовый дифф со всеми атрибутами эддед, ченджед.
def format_value(value):
    return str(value).lower() if isinstance(value, bool) else str(value)


def format_data(diff):
    formatted_lines = ''
    for node in diff:
        status = node['status']
        depth = node['depth']
        intent = '  ' * depth
        key = node['key']
        value = node.get('value')
        value_old = node.get('value_old')
        value_new = node.get('value_new')
        #print(status, depth, key, value, value_new, value_old)
        if status == 'unchanged':
            formatted_lines = formatted_lines + (f'{intent}  {key}: {value}\n')
        elif status == 'deleted':
            formatted_lines = formatted_lines + (f'{intent}- {key}: {value}\n')
        elif status == 'added':
            formatted_lines = formatted_lines + (f'{intent}+ {key}: {value}\n')
        elif status == 'changed':
            formatted_lines = formatted_lines + (f'{intent}- {key}: {value_old}\n')
            formatted_lines = formatted_lines + (f'{intent}+ {key}: {value_new}\n')
        elif status == 'nested':
            value_nest = format_data(value)
            #print(value_nest)
            formatted_lines = formatted_lines + '{' + '\n' + (f'{intent * depth}  {key}: \n {value_nest}\n')
           
    return formatted_lines


# formatted_str = "{\n" + format_data(data, 1) + "\n}"
# print(formatted_str)
