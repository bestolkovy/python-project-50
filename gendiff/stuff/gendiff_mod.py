def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def generate_diff(file1, file2):
    all_keys = set(file1.keys()).union(file2.keys())
    diff_lines = []
    for key in sorted(all_keys):
        value1 = file1.get(key)
        value2 = file2.get(key)
        if value1 is None:
            diff_lines.append(f"  + {key}: {format_value(value2)}")
        elif value2 is None:
            diff_lines.append(f"  - {key}: {format_value(value1)}")
        elif value1 != value2:
            diff_lines.append(f"  - {key}: {format_value(value1)}")
            diff_lines.append(f"  + {key}: {format_value(value2)}")
        else:
            diff_lines.append(f"    {key}: {format_value(value1)}")

    return "{\n" + "\n".join(diff_lines) + "\n}"
