from gendiff import parsing
# нам надо два словаря


def diff_build(dict1, dict2):
    all_keys = set(dict1.keys()).union(dict2.keys())
    diff = {}
    for key in all_keys:
        if key not in dict2:
            diff[key] = {'status': 'deleted', 'value': dict1[key]}
        elif key not in dict1:
            diff[key] = {'status': 'added', 'value': dict2[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = diff_build(dict1[key], dict2[key])
            diff[key] = {'status': 'nested', 'value': nested_diff}
        elif dict1[key] == dict2[key]:
            diff[key] = {'status': 'unchanged', 'value': dict1[key]}
        else:
            diff[key] = {'status': 'changed', 'value_old': dict1[key],
                         'value_new': dict2[key]}

    return diff


dic1 = parsing('/home/corleone/python-project-50/tests/fixtures/nested1.json')
dic2 = parsing('/home/corleone/python-project-50/tests/fixtures/nested2.json')

diff = diff_build(dic1, dic2)
print(diff)