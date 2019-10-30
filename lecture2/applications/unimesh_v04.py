#!/usr/bin/env python3
"""Generate a mesh in square domain.
"""

import argparse
from math import *

def handleCommandLine():
    parser = argparse.ArgumentParser(description='Generate a mesh in square domain.')
    parser.add_argument('--nnodes', metavar='N', 
                     action='store',
                     dest='nnodes',
                     required=False,
                     type=int,
                     default=2,
                     help='number of nodes per side')
    parser.add_argument('-L',
                     action='store',
                     dest='side',
                     required=False,
                     type=float, 
                     default=1.0,
                     help='square side length')
    parser.add_argument('--elevation', action='store',
                        dest='elevation', required=False,
                        default='0.0', help='elevation expression of (x,y)')

    args = parser.parse_args()
    return args


def fakeGeneration(nnodes=2, side=1.0):
    """Mesh generation mockup.
    """
    print("Generating mesh:")
    print("   side length: %f"  %side);
    print("   number of nodes per side: %d" % nnodes)

def makePoints(nnodes=2, side=1.0):
    """Generate list of 3D points on Cartesian grid in XY plane.
    """
    L = side/(nnodes-1)
    xc = [L*i for i in range(nnodes)]
    yc = xc
    points = [(x,y, 0.0) for x in xc for y in yc]
    #points = itertools.product(x,y) # other way
    return points

def writeMesh(fname, nx, ny,  points):
    out = open(fname, 'w')
    out.write('MESH\n')
    out.write("%d %d\n" % (nx,ny))
    for p in points:
        out.write("%f %f %f\n" % p)

def elevator(expr, point):
    x,y,z = point
    return (x,y, eval(expr))

if __name__ == '__main__':
    cmdl = handleCommandLine()
    nx = ny = cmdl.nnodes
    fakeGeneration(nx, cmdl.side)
    points = makePoints(nx, cmdl.side)
    points = map(lambda p: elevator(cmdl.elevation,p), points) 
    writeMesh("square.mesh", nx, ny, points)
