def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    

def format_key(node): # нод список с ключами
    if node['status'] == 'nested':
        subkey = node['key']



def plain(data):
    result = ''
    for item in data:
        status = item['status']
        key = item['key']
        depth = item['depth']
        value = item.get('value', None)
        if status == 'nested':
            for huy in value:
                subkey = key
                subkey += f".{huy['key']}"
                result += f"{subkey}.\n" 
        if status == 'added':
            result += f"Property '{key}' was added with value: '{format_value(value)}'\n"
        if status == 'deleted':
            result += f"Property '{key}' was removed\n"
        if status == 'changed':
            value_old = format_value(item['value_old'])
            value_new = format_value(item['value_new'])
            result += f"Property {key}' was update. From '{value_old}' to '{value_new}'\n"
        if status == 'unchanged':
            result = result
    return result
