#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import re
import itertools
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'speedupghost.log'), level = logging.DEBUG)  

libs = [{'google': 'libs.googleapis.com', 'useso': 'libs.useso.com'},
        {'google': 'ajax.googleapis.com', 'useso': 'ajax.useso.com'},
        {'google': 'fonts.googleapis.com', 'useso': 'fonts.useso.com'}
]
org = 'google'
dest = 'useso'


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