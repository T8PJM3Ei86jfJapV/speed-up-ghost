#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import re
import itertools
import logging

logging.basicConfig(filename = os.path.splitext(__file__)[0] + '.log', level = logging.DEBUG)

libs = [{'google': 'ajax.googleapis.com', 'useso': 'ajax.useso.com', 'ustc': 'ajax.lug.ustc.edu.cn'},
        {'google': 'fonts.googleapis.com', 'useso': 'fonts.useso.com', 'ustc': 'fonts.lug.ustc.edu.cn'}
]

# libs[#][dest] will take over libs[#][org]
org = 'google'
dest = 'ustc'

def gen_new_file(fileName):
    # backup old file and build log
    oldFile = fileName + '.old'
    os.rename(fileName, oldFile)
    logging.info('[' + fileName + '] -> [' + oldFile + ']')

    # read lines and make destinate url take over orginal url
    lines = list()
    with open(oldFile, 'r') as f:
        lines = f.readlines()
        for index, lib in itertools.product(range(len(lines)), libs):
            lines[index] = re.sub(lib[org], lib[dest], lines[index])

    # write lines into a new file
    with open(fileName, 'w') as f:
        f.writelines(lines)

def contains_key_strings(fileName):
    with open(fileName, 'r') as f:
        for line, lib in itertools.product(f.readlines(), libs):
            if re.search(lib[org], line):
                return True
    return False

def main():
    root = os.path.join(os.getcwd(), '..')
    exception = os.path.join(root, 'tools')
    for path, dirs, files in os.walk(root):
        for name in files:
            fileName = os.path.join(path, name)
            if exception not in fileName and os.path.splitext(fileName)[1] != '.old' and contains_key_strings(fileName):
                gen_new_file(fileName)

if __name__ == "__main__":
    main()