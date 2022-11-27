#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Define factory for different quadratures
"""
import newtoncotes 
import gausslegendre

def known_quadratures():
    return ["NewtonCotes", "GaussLegendre"]

def make_quadrature(name, nnodes):
    if name == "NewtonCotes":
        return newtoncotes.NewtonCotes(nnodes)
    elif name == "GaussLegendre":
        return gausslegendre.GaussLegendre(nnodes)
    raise RuntimeError("Invalid quadrature %s %d" %(name, nnodes))  
