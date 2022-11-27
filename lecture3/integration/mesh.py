# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Define 1D Mesh class
"""

class Mesh(object):
     """Represents on dimensional mesh
     """
     def __init__(self):
         self.nodes = list()

     def load(self, filename):
         """Read from file a list of nodes"""
         with open(filename, 'r') as f:
             for l in f:
                 self.nodes.append(tuple(float(x) for x in l.split()))

     def nelem(self):
         return len(self.nodes)-1
