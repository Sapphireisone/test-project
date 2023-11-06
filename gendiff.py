import json


def parse(file_path: str):
    file = json.load(open(file_path))
    return file


file1 = parse('file1.json')
file2 = parse('file2.json')


def gendiff(file1, file2, res=[], str=''):
    for key in file1:
        result = {}
        if type(file1[key]) != dict:
            if key not in file2:
                result['attribute'] = f'{str}{key}'
                result['type'] = 'deleted'
                result['value'] = file1[key]
            else:
                if file1.get(key) == file2.get(key):
                    result['attribute'] = f'{str}{key}'
                    result['type'] = 'unchanged'
                    result['value'] = file1[key]
                else:
                    result['attribute'] = f'{str}{key}'
                    result['type'] = 'changed'
                    result['value from'] = file1[key]
                    result['value to'] = file2[key]
        else:
            str += f'{key}.'
            gendiff(file1[key], file2[key], res, str)
        if result:
            res.append(result)
    for key in file2:
        result = {}
        if type(file2[key]) != dict:
            if key not in file1:
                result['attribute'] = f'{str}{key}'
                result['type'] = 'added'
                result['value'] = file2[key]
        else:
            str += f'{key}.'
            gendiff(file1[key], file2[key], res, str)
        if result:
            res.append(result)
    return res


res = gendiff(file1, file2)
print(res)
