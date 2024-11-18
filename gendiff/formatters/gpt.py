import json



def simplify_diff(diff):
    def process_item(item):
        key = item['key']
        status = item['status']
        
        def convert_value(val):
            # Конвертация строк "False", "True", "None" в реальные Python-значения
            if val == "False":
                return False
            elif val == "True":
                return True
            elif val == "None":
                return None
            return val

        if status == 'changed':
            return {
                key: {
                    "status": status,
                    "old_value": convert_value(item.get("value_old")),
                    "new_value": convert_value(item.get("value_new"))
                }
            }
        elif status in ('deleted', 'added', 'unchanged'):
            return {
                key: {
                    "status": status,
                    "value": convert_value(item.get("value"))
                }
            }
        elif status == 'nested':
            nested_value = {sub_item['key']: process_item(sub_item)[sub_item['key']] for sub_item in item['value']}
            return {key: {"status": status, "value": nested_value}}
        
        return {key: {}}

    return {item['key']: process_item(item)[item['key']] for item in diff}


# Загрузка файла диффа
with open('/home/corleone/python-project-50/tests/fixtures/diff.txt', 'r', encoding='utf-8') as file:
    diff = eval(file.read().strip().replace('false', 'False').replace('null', 'None').replace('true', 'True'))


# Преобразование и вывод результата
simplified_diff = simplify_diff(diff)
print(json.dumps(simplified_diff, indent=2, ensure_ascii=False))
