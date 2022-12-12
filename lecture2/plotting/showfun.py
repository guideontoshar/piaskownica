"""Plot a function.
"""

import argparse
from math import *
import matplotlib.pyplot as plt

def handleCommandLine():
    parser = argparse.ArgumentParser(description='Plot a function.')
    parser.add_argument('--xrange', metavar='N', 
                     action='store',
                     dest='xrange',
                     required=False,
                     default='(0.0, 6.0)',
                     help='xrange')
    parser.add_argument('function', nargs='?', default='sin(x)', action='store',
                         help='function f(x)')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    cmdl = handleCommandLine()
    N = 100
    xb,xe=eval(cmdl.xrange)
    dx = (xe-xb)/(N-1)
    xc = [i*dx for i in range(N)]
    yc = list(map(lambda x: eval(cmdl.function), xc))
    plt.title(cmdl.function)
    plt.plot(xc,yc)
    plt.show()
