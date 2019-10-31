# -*- coding: utf-8 -*-
"""
Illustrate creation of quad mesh in rectangle
by four-corners mapping
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def meshpoints(radius, nx, ny):
    """Return points of Cartesian nx by ny grid projected on a disk of give
    radius
    """
    x = np.linspace(-1.0, 1.0, nx)
    y = np.linspace(-1.0, 1.0, ny)
    xx, yy = np.meshgrid(x, y)
    cx = radius * xx * np.sqrt(1-yy**2/2)
    cy = radius * yy * np.sqrt(1-xx**2/2)
    points = np.c_[cx.flatten(), cy.flatten()]
    return points


def main():
    radius = 2
    nx, ny = 10, 10

    fig, ax = plt.subplots()

    points = meshpoints(radius, nx, ny)
    mesh = matplotlib.collections.QuadMesh(nx-1, ny-1, points, edgecolors='black',
                                           facecolors='yellow')
    ax.add_collection(mesh)
    ax.autoscale()
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    main()