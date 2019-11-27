#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Newton-Cotes numerical integration formulas
"""

class NewtonCotes:
     _weights = { 2: (0.5, 0.5),
                  3 : tuple(x/6.0 for x in (1, 4, 1))
                }
  
    def __init__(self, nnodes):
        self.ref_weights = self._weights[nnodes]
        self.degree = len(self.ref_weights)-1
  
    def nodes(self, a=0.0, b=1.0):
        n = len(self.ref_weights)
        dx = (b-a)/(n-1)
        return [a+i*dx for i in range(n)]
  
    def weights(self, a=0.0, b=1.0):
        return ((b-a)*x for x in self.ref_weights)

class TrapezoidQuadrature(NewtonCotes):
    def __init__(self):
        super().__init__(2)

class SimpsonQuadrature(NewtonCotes):
    def __init__(self):
        super().__init__(3)

if __name__ == '__main__':
    qr = TrapezoidQuadrature()
    a = -3;
    b = 5;
    if abs(sum(qr.weights(a,b)) - (b-a)) < 1.e-8:
        print("Tesing weights: OK")
    else:
        print("Testing weights: FAILED")
    print("TrapezoidQuadrature degree: ", qr.degree)

    qr = SimpsonQuadrature()
    if abs(sum(qr.weights(a,b)) - (b-a)) < 1.e-8:
        print("Tesing weights: OK")
    else:
        print("Testing weights: FAILED")
    print("SimpsonQuadrature degree: ", qr.degree)
