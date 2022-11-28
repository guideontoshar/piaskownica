"""The purpose of this script is to draw regular n-sided polygon
"""

import numpy
import matplotlib.patches
import matplotlib.pyplot as plt


def get_vertices(nsides=3, radius=1.0, center=(0.0, 0.0), start_angle=0.0):
    """Return list of coordinates of vertices for regular nsided polygon.
    """
    angles = numpy.linspace(0.0, 360.0, nsides+1, dtype='float') + start_angle
    numpy.radians(angles, angles)
    x = radius * numpy.cos(angles) + center[0]
    y = radius * numpy.sin(angles) + center[1]
    return x, y


def plot_polygon(ax, x, y, facecolor='yellow'):
    """Plot polygon given by vertex coordinates
    """
    vertices=list(zip(x, y))
    poly = matplotlib.patches.Polygon(vertices, facecolor=facecolor, edgecolor='black')
    ax.add_patch(poly)


if __name__ == '__main__':
    nsides = 4
    radius = 2.0
    start_angle = 0
    center = (0.0, 0.0)
    x, y = get_vertices(nsides, radius, center, start_angle)
    fig, ax = plt.subplots()
    plot_polygon(ax, x, y)
    ax.autoscale()
    ax.set_aspect('equal')
    fig.show()
    plt.show()
