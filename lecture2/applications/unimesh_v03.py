"""Generate a mesh in square domain.
"""

import argparse

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
    """Write mesh in geomview MESH format to file under given name.
    """
    out = open(fname, 'w')
    out.write('MESH\n')
    out.write("%d %d\n" % (nx,ny))
    for p in points:
        out.write("%f %f %f\n" % p)

def elevator(point):
    """Calculate new point as function of x,y.
    """
    x,y,z=point
    return(x,y,x*y)

if __name__ == '__main__':
    cmdl = handleCommandLine()
    nx = ny = cmdl.nnodes
    fakeGeneration(nx, cmdl.side)
    points = makePoints(nx, cmdl.side)
    points = map(elevator, points) 
    writeMesh("square.mesh", nx, ny, points)
