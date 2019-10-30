"""Simple cript to illustrate basic handling of commmand
line arguments.
"""

import sys

def args_printer():
    """Print command line argument.
    """
    if len(sys.argv) > 1:
        for i, arg  in enumerate(sys.argv[1:], start=1):
            print("Argument %d : %s" % (i, arg))
    else:
        print('No command line argument given')

if __name__ == '__main__':
    args_printer()
