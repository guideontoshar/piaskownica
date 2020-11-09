# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:14:53 2020

@author: putanowr
"""

import colorama
import numpy
from colorama import Fore

colors = {'green' : Fore.GREEN,
          'white' : Fore.WHITE }

class Rectangle:
    def __init__(self, width, height, color='white'):
        self.W = width
        self.H = height
        self.symbols = numpy.empty((self.H, self.W), dtype='object_')
        self.symbols.fill('*')
        self.colors = numpy.empty((self.H, self.W), dtype='object_')
        self.colors.fill(colors[color])
        
    def size(self):
        return self.W, self.H
    
class TriangleUp:
    def __init__(self, height, color='white'):
        self.H = height
        self.W = 2*height-1
        self.colors = numpy.empty((self.H, self.W), dtype='object_')
        self.colors.fill(colors[color])
        self.symbols = numpy.empty((self.H, self.W), dtype='object_')
        self.symbols.fill('')
        for i in range(self.H):
            self.symbols[i, i:self.W-i] = '*'
    def size(self):
        return self.W, self.H
            
class GiftBox:
    def __init__(self):
        self.symbols = numpy.array([['*','*','*'],['*','*','*'],
                                    ['*','*','*']], dtype='object_')
        self.colors = numpy.empty((3,3), dtype='object_')
        self.colors.fill(colorama.Fore.WHITE)
        self.colors[:,1] = colorama.Fore.RED
        self.colors[1,:] = colorama.Fore.RED
    def size(self):
        return (3,3)
    
class AsciiWorld:
    def __init__(self, width, height):
        self.symbols = numpy.empty((height, width), dtype='object_')
        self.colors = numpy.empty((height, width), dtype='object_')
        self.H = height
        self.W = width
        self.symbols.fill(' ')
        self.colors.fill(f"{colorama.Back.BLUE}")

    def add(self, item, x, y):
        w,h = item.size()
        for i in range(h):
            for j in range(w):
                if item.symbols[i,j] != '':
                    px=y+i
                    py=x+j
                    if px >=0 and px< self.H and py>=0 and py< self.W:
                        self.symbols[px, py] = item.symbols[i,j]       
                        self.colors[px, py] = item.colors[i,j]
    
    def print(self):
        for i in range(self.H-1, -1, -1):
            s=''
            for j in range(self.W):
                s+=f"{self.colors[i,j]}{self.symbols[i,j]}"
            print(s, end='')
            print(colorama.Style.RESET_ALL, end='')
            print('',end='\n')
        print('My picture')
                
if __name__ == '__main__':
    world = AsciiWorld(80, 60)
    world.add(GiftBox(), 10, 0)
    world.add(TriangleUp(20, 'white'), 60, 7)
    world.add(Rectangle(3, 7), 28, 0)
    world.add(TriangleUp(10, 'green'), 20, 3)
    world.print()
    