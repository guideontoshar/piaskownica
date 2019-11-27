# -*- coding: utf-8 -*-

"""
Demonstrate how to use Polygon objects.
"""

from class_polygon import Polygon
import matplotlib.patches
import matplotlib.pyplot as plt

if __name__ == '__main__':
    polys = [Polygon(6, 3.0, start_angle=30),
             Polygon(4, 1.0, (1.0, 1.0))]

    fig, ax = plt.subplots()
    colors = ['yellow', 'red']
    for poly, color in zip(polys, colors):
        poly.plot(ax, facecolor=color)
        print('Polygons sides : ', poly.nsides)

    ax.autoscale()
    ax.set_aspect('equal')
    fig.show()
