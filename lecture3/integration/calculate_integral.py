#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Calculate integral of scalar function in 1D
"""
import itertools
import argparse
import quadratures

from mesh import Mesh
from integrands import Integrand
from integrators import MeshIntegrator

def parse_command_line():
    """Parse command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quadrature', dest='quadrature',
                        default='NewtonCotes',
                        choices = quadratures.known_quadratures())
    parser.add_argument("-n", '--nodes', type=int, dest='nnodes', default=2,
                        help="number of quadrature nodes")
    parser.add_argument("-i", '--integrand', default='x**2', dest='integrand',
                        help="expression to be integrated")
    parser.add_argument("meshfile", help="name of the mesh file")
    args = parser.parse_args()
    return args
 
def main():
    args = parse_command_line()
    mesh = Mesh()
    mesh.load(args.meshfile)
    integrand = Integrand(args.integrand)
    quadrature = quadratures.make_quadrature(args.quadrature, args.nnodes)
    integrator = MeshIntegrator()
    integral = integrator.integrate(mesh, integrand, quadrature)
    print("Integral of %s is %g" %(args.integrand, integral))
 
if __name__ == '__main__':
    main()
