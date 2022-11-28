# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:14:53 2020

@author: putanowr
"""

import colorama
import numpy

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
        self.symbols[y:y+h, x:x+w] = item.symbols       
        self.colors[y:y+h, x:x+w] = item.colors
    
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
    world = AsciiWorld(80, 20)
    world.add(GiftBox(), 10, 0)
    world.print()
 
