import os
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path=os.getcwd()

    for s in os.listdir(path):
        print(s)
