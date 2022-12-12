"""The purpose of this script is to demonstrate implementation of polygon as a class
"""

import numpy
import matplotlib.patches


class Polygon:
    def __init__(self, nsides=3, radius=1.0, center=(0.0, 0.0), start_angle=0.0):
        self.nsides = nsides
        self.radius = radius
        self.center = center
        self.start_angle = start_angle

    def get_vertices(self):
        """Return list of coordinates of vertices for regular nsided polygon.
        """
        angles = numpy.linspace(0.0, 360.0, self.nsides+1, dtype='float') + self.start_angle
        numpy.radians(angles, angles)
        x = self.radius * numpy.cos(angles) + self.center[0]
        y = self.radius * numpy.sin(angles) + self.center[1]
        return x, y

    def plot(self, ax, facecolor='yellow'):
        """Plot polygon given by vertex coordinates
        """
        x, y = self.get_vertices()
        vertices = list(zip(x, y))
        poly = matplotlib.patches.Polygon(vertices, facecolor=facecolor, edgecolor='black')
        ax.add_patch(poly)

