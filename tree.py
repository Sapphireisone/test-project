import json
import hexlet.fs as fs
from gendiff_2 import parse


file1 = parse('file1.json')
file2 = parse('file2.json')


def dfs(node):
    print(fs.get_name(node))
    if fs.is_file(node):
        return
    children = fs.get_children(node)
    list(map(dfs, children))


dfs(file1)
