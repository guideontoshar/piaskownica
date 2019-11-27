# -*- coding: utf-8 -*-

"""
Demonstrate how represent polygon as dictionary.
"""

import polygon
import matplotlib.patches
import matplotlib.pyplot as plt

def get_vertices(poly):
    return polygon.get_vertices(poly['nsides'],
                                poly['radius'],
                                poly['center'],
                                poly['start_angle'])


if __name__ == '__main__':
    polys = [{'nsides': 6, 'radius' : 3.0, 'center': (0.0, 0.0), 'start_angle': 30},
             {'nsides': 4, 'radius' : 1.0, 'center': (1.0, 1.0), 'start_angle': 0}
    ]

    fig, ax = plt.subplots()
    for poly in polys:
        x, y = get_vertices(poly)
        polygon.plot_polygon(ax, x, y)

    ax.autoscale()
    ax.set_aspect('equal')
    fig.show()
