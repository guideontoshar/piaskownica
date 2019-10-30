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

def main():
    """The starting function of the application.
    """
    cmdl = handle_command_line()
    fake_generation(cmdl.nnodes, cmdl.side)

if __name__ == '__main__':
    main()
