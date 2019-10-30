import os
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path=os.getcwd()

    if len(sys.argv) > 2:
        pattern = sys.argv[2]
    else:
        pattern = '.*'

    fileFilter = re.compile(pattern)

    for s in os.listdir(path):
        if fileFilter.match(s):
            print(s)
