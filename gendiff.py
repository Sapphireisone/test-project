import json


def parse(file_path: str):
    file = json.load(open(file_path))
    return file


file1 = parse('file1.json')
file2 = parse('file2.json')


def gendiff(file1, file2):
    file1 = dict(sorted(file1.items(), key=lambda x: x[0])) if file1 else {}
    file2 = dict(sorted(file2.items(), key=lambda x: x[0])) if file2 else {}
    res = []
    for key in file1:
        result = {}
        if type(file1[key]) is not dict:
            if key not in file2:
                result['attribute'] = f'{key}'
                result['type'] = 'deleted'
                result['value'] = file1[key]
            else:
                if file1.get(key) == file2.get(key):
                    result['attribute'] = f'{key}'
                    result['type'] = 'not changed'
                    result['value'] = file1[key]
                else:
                    result['attribute'] = f'{key}'
                    result['type'] = 'changed'
                    result['value from'] = file1[key]
                    result['value to'] = file2[key]
        else:
            gendiff(file1[key], file2[key])
        if result:
            res.append(result)
    for key in file2:
        result = {}
        if type(file2[key]) is not dict:
            if key not in file1:
                result['attribute'] = f'{key}'
                result['type'] = 'added'
                result['value'] = file2[key]
        else:
            gendiff(file1[key], file2[key])
        if result:
            res.append(result)
    return res


res = gendiff(file1, file2)
print(res)
