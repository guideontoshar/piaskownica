# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 putanowr <putanowr@foo>
#
# Distributed under terms of the MIT license.

"""
Define integrand function
"""

class Integrand(object):
  """Represents integrand as 1D scalar function
  """
  def __init__(self, expression):
    self.expression = expression

  def evaluate(self, x):
    return eval(self.expression)

  def __call__(self, x):
    return self.evaluate(x)
