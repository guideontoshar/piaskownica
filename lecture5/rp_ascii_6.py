# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:14:53 2020

@author: putanowr
"""

import colorama
import numpy
from colorama import Fore

colors = {'green' : Fore.GREEN,
          'white' : Fore.WHITE,
          'black' : Fore.BLACK,
          'red'   : Fore.RED}

class AsciiItem:
    def __init__(self, width=0, height=0, color='white', char='*'):
       self.W = width
       self.H = height
       self._size = (self.H, self.W)
       self.symbols = numpy.empty(self.size, dtype='object_')
       self.symbols.fill(char)
       self.colors = numpy.empty(self.size, dtype='object_')
       self.colors.fill(colors[color])
        
    @property
    def size(self):
        return self._size
        
class Rectangle(AsciiItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def anchor(self):
        return (self.W//2, 0)
    
class TriangleUp(AsciiItem):
    def __init__(self, height, color='white', char='*'):
        W = 2*height-1
        super().__init__(width=W, height=height, color=color, char='')
        for i in range(self.H):
            self.symbols[i, i:self.W-i] = char
      
    def anchor(self):
        return (self.W//2, 0)   
    
class GiftBox:
    def __init__(self):
        self.symbols = numpy.array([['*','*','*'],['*','*','*'],
                                    ['*','*','*']], dtype='object_')
        self.colors = numpy.empty((3,3), dtype='object_')
        self.colors.fill(colorama.Fore.WHITE)
        self.colors[:,1] = colorama.Fore.RED
        self.colors[1,:] = colorama.Fore.RED
    
    @property
    def size(self):
        return (3,3)

    def anchor(self):
        return (1,0)
    
class AsciiWorld:
    def __init__(self, width, height):
        self.symbols = numpy.empty((height, width), dtype='object_')
        self.colors = numpy.empty((height, width), dtype='object_')
        self.H = height
        self.W = width
        self.symbols.fill(' ')
        self.colors.fill(f"{colorama.Back.BLUE}")

    def add(self, item, x, y):
        h,w = item.size
        ax,ay = item.anchor()
        for i in range(h):
            for j in range(w):
                if item.symbols[i,j] != '':
                    px=y+i-ay
                    py=x+j-ax
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
    world.add(GiftBox(), 25, 0)
    world.add(TriangleUp(20, color='white'), 60, 7)
    world.add(Rectangle(width=3, height=7, color='green'), 60, 3)
    world.add(Rectangle(width=3, height=7), 20, 0)
    world.add(TriangleUp(10, color='green', char='#'), 20, 5)
    world.print()
    
