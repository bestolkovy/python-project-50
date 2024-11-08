from gendiff import parsing
from gendiff import formatted_diff
from gendiff import diff_build


def generate_diff(path1, path2, formatter='stylish'):
    dict1 = parsing(path1)
    dict2 = parsing(path2)
    diff = diff_build(dict1, dict2)
    return formatted_diff(diff, formatter)
