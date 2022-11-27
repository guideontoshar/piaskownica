#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Gauss-Legender numerical integration formulas
"""
import itertools
import math
from math import sqrt

def antisymmetrize(seq, central=tuple()):
    return list(itertools.chain([-x for x in seq[::-1]], central, seq))

def symmetrize(seq, central=tuple()):
    return list(itertools.chain(seq[::-1], central, seq))

class GaussLegendre(object):
  _nodes = { 1: [0.0],
             2: antisymmetrize([sqrt(1.0/3.0)]),
             3: antisymmetrize([sqrt(3.0/5.0)], [0.0]),
             4: antisymmetrize([sqrt((3-2*sqrt(6/5))/7), 
                                sqrt((3+2*sqrt(6/5))/7)])
           }
  _weights = { 1: [2.0], 
               2: symmetrize([1.0]),
               3: symmetrize([5/9], [8/9]),
               4: symmetrize([(18+sqrt(30))/36,
                              (18-sqrt(30))/36])
             }

  def __init__(self, nnodes):
    self.ref_nodes = self._nodes[nnodes]
    self.ref_weights = self._weights[nnodes]

  def nodes(self, a=0.0, b=1.0):
    shift = (a+b)/2
    scale = (b-a)/2                   
    return [shift + scale*x for x in self.ref_nodes]

  def weights(self, a=0.0, b=1.0):
    jacobian = (b-a)/2
    return [jacobian*w for w in self.ref_weights]

if __name__ == '__main__':
    qr = GaussLegendre(4)
    a = -3;
    b = 5;
    weights_sum = sum(qr.weights(a,b))
    if abs(weights_sum - (b-a)) < 1.e-8:
        print("Tesing weights: OK")
    else:
        print("Testing weights: FAILED %f" % weights_sum)
