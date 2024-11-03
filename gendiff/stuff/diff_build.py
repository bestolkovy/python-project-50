def format_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    #else:
        #value = str(value)
    if value == 'None':
        value = 'null'
    return value


def diff_build(dict1, dict2, depth=0):
    all_keys = dict1.keys() | dict2.keys()
    #print (sorted(all_keys))
    diff = []
    for key in sorted(all_keys):
        if key not in dict2:
            diff.append({'status': 'deleted', 'key': key, 'depth': depth, 'value': format_value(dict1[key])})
        elif key not in dict1:
            diff.append({'status': 'added', 'key': key, 'depth': depth, 'value': format_value(dict2[key])})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = diff_build(dict1[key], dict2[key], depth+1)
            diff.append({'status': 'nested', 'key': key, 'depth': depth, 'value': nested_diff})
        elif dict1[key] == dict2[key]:
            diff.append({'status': 'unchanged', 'key': key, 'depth': depth, 'value': format_value(dict1[key])})
        else:
            diff.append({'status': 'changed', 'key': key, 'depth': depth, 'value_old': format_value(dict1[key]),
                         'value_new': format_value(dict2[key])})
    #print(diff)        
    return diff
