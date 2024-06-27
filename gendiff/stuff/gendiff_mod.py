def generate_diff(dict_a, dict_b):
    all_keys = set(dict_a.keys()).union(dict_b.keys())
    result = []
    for key in sorted(all_keys):
        if key in dict_a and key in dict_b:
            if dict_a[key] != dict_b[key]:
                result.append(f"  - {key}: {dict_a[key]}")
                result.append(f"  + {key}: {dict_b[key]}")
            else:
                result.append(f"    {key}: {dict_a[key]}")
        elif key in dict_a:
            result.append(f"  - {key}: {dict_a[key]}")
        elif key in dict_b:
            result.append(f"  + {key}: {dict_b[key]}")
    result_str = "{\n" + "\n".join(result) + "\n}"
    return result_str
