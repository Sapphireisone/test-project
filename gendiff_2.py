import json


def parse(file_path: str):
    file = json.load(open(file_path))
    return file


file1 = parse('file1.json')
file2 = parse('file2.json')


def gendiff(data1, data2, lst=[]):
    keys = list(data1.keys() | data2.keys())
    keys.sort() if keys else []
    for key in keys:
        data1.get(key, 'default')
        if isinstance(data1[key], dict):
            gendiff(data1[key], data2[key], lst)
        else:
            result = {'attribute': key}
            if key not in data1:
                result['type'] = 'added'
                result['value'] = file2[key]
            elif key not in data2:
                result['type'] = 'deleted'
                result['value'] = file1[key]
            elif data1[key] == data2[key]:
                result['type'] = 'unchanged'
                result['value'] = file1[key]
            else:
                result['type'] = 'changed'
                result['value from'] = file1[key]
                result['value to'] = file2[key]
            lst.append(result)
    return result


res = gendiff(file1, file2)
print(res)