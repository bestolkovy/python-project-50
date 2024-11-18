import json
import re


def convert_json(data):
    result = json.dumps(data, indent=2)
    pattern = r'"(false|true|null)"'
    result = re.sub(pattern, r'\1', result)
    return result
