"""Generate a mesh in square domain.
"""

import argparse

def handle_command_line():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description=\
        'Generate a mesh in square domain.')
    parser.add_argument('--nnodes', metavar='N',\
            action='store',\
            dest='nnodes',\
            required=False,\
            type=int,\
            default=2,\
            help='number of nodes per side')
    parser.add_argument('-L',\
            action='store',\
            dest='side',\
            required=False,\
            type=float,\
            default=1.0,\
            help='square side length')

    args = parser.parse_args()
    return args

def fake_generation(nnodes=2, side=1.0):
    """Mesh generation mockup.
    """
    print("Generating mesh:")
    print("   side length: %f"  %side)
    print("   number of nodes per side: %d" % nnodes)

def make_points(nnodes=2, side=1.0):
    """Generate list of 3D points on Cartesian grid in XY plane.
    """
    sdx = side/(nnodes-1)
    xcoords = [sdx*i for i in range(nnodes)]
    ycoords = xcoords
    points = [(x, y, 0.0) for x in xcoords for y in ycoords]
    #points = itertools.product(x,y) # other way
    return points

def write_mesh(fname, nx, ny,  points):
    """Write mesh in geomview MESH format to file under given name.
    """
    out = open(fname, 'w')
    out.write('MESH\n')
    out.write("%d %d\n" % (nx, ny))
    for p in points:
        out.write("%f %f %f\n" % p)

def main():
    """The starting function of the application.
    """
    cmdl = handle_command_line()
    nx = ny = cmdl.nnodes
    fake_generation(cmdl.nnodes, cmdl.side)
    points = make_points(nx, cmdl.side)

    write_mesh("square.mesh", nx, ny, points)

if __name__ == '__main__':
    main()
