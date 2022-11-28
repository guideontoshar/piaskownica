# -*- coding: utf-8 -*-

"""
Demonstrate how to use polygon module to draw some polygons.
"""

import polygon
import matplotlib.patches
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nsides = [6, 4]
    radius = [3.0, 1.0]
    center = [(0.0, 0.0), (1.0, 1.0)]
    start_angle = [30.0, 0.0]

    fig, ax = plt.subplots()
    for i in range(len(nsides)):
        x, y = polygon.get_vertices(nsides[i], radius[i], center[i], start_angle[i])
        polygon.plot_polygon(ax, x, y)

    ax.autoscale()
    ax.set_aspect('equal')
    fig.show()
    plt.show()
