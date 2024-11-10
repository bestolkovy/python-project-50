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
                result += f'{subkey}\n' 
        if status == 'added':
            result += f'Property {key} was added with value: {value}\n'
        if status == 'deleted':
            result += f'Property {key} was removed\n'
        if status == 'changed':
            result += f'Property {key} was update. From {item["value_old"]} to {item["value_new"]}\n'
    return result
