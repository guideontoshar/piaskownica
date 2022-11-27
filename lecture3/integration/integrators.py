#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Integrate function over a mesh
"""
import itertools

class MeshIntegrator:
    """Calculate integral over a domain discretised by a mesh
    """

    def integrate(self, mesh, integrand, quadrature):
        """Integrate function fun using numerical integration on given mesh
        """
        integral = 0.0
        for i in range(mesh.nelem()):
            integral += self.integrate_element(i, mesh, integrand, quadrature)
        return integral
 
    def make_mesh_fun(self, mesh, fun):
        xcoord = [ node[0] for node in mesh.nodes ]
        discrete_fun = [ fun(x) for x in xcoord ] 
        return discrete_fun 
 
    def integrate_element(self, i, mesh, integrand, quadrature):
        x1 = mesh.nodes[i][0]
        x2 = mesh.nodes[i+1][0]
        qr = quadrature
        integral = 0.0
        for (x, w) in itertools.zip_longest(qr.nodes(x1, x2), qr.weights(x1,x2)):
            integral += w * integrand(x);
        return integral
