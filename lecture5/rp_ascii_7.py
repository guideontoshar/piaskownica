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
          'red'   : Fore.RED,
          'inherit' : ''}

class AsciiItem:
    def __init__(self, width=0, height=0, fgcolor='white', bgcolor='inherit', char='*'):
       self.W = width
       self.H = height
       self._size = (self.W, self.H)
       self._anchor = (0,0)
       s = (self.H, self.W)
       self.symbols = numpy.empty(s, dtype='object_')
       self.symbols.fill(char)
       self.bgcolors = numpy.empty(s, dtype='object_')
       self.bgcolors.fill(colors[bgcolor])
       self.fgcolors = numpy.empty(s, dtype='object_')
       self.fgcolors.fill(colors[fgcolor])
       
    def add(self, item, x, y):
        w, h = item.size
        ax,ay = item.anchor
        for i in range(w):
            for j in range(h):
                if item.symbols[j,i] != '':
                    py=y+j-ay
                    px=x+i-ax
                    if py >=0 and py< self.H and px>=0 and px< self.W:
                        self.symbols[py, px] = item.symbols[j,i]  
                        if item.bgcolors[j,i] != colors['inherit']:
                            self.bgcolors[py, px] = item.bgcolors[j,i]
                        if item.fgcolors[j,i] != colors['inherit']:
                            self.fgcolors[py, px] = item.fgcolors[j,i]  
    
    @property
    def SW(self):
        return (0,0)
    
    @property
    def SE(self):
        return (self.W-1, 0)
    
    @property
    def NE(self):
        return (self.W-1, self.H-1)
    
    @property
    def NW(self):
        return (0, self.H-1)
    
    @property
    def size(self):
        return self._size
    
    @property
    def anchor(self):
        return self._anchor

class StripesDecorator:
    def __init__(self, char="o", color='red', step=2, direction=(1,1)):
        self.char = char
        self.color = color
        self.step = step
        self.direction = direction
        
    def _start(self, item):
        selector = tuple(x >= 0 for x in self.direction)
        sp = {(1,1)  : item.SW, 
              (0, 1) : item.SE,
              (0, 0) : item.NE,
              (1, 0) : item.NW}
        return sp[selector]
    
    def __call__(self, item):
        W,H = item.size
        M = max(W,H)
        x,y = self._start(item)
        for si in range(0, W, self.step):
            x,y = self._start(item)
            x += si* (1 if self.direction[0] >= 0 else -1)
            for i in range(0, M):
                self._decorate(item, x, y)
                x += self.direction[0]
                y += self.direction[1]
        x,y = self._start(item)        
        for sj in range(0, H, self.step):
            x,y = self._start(item)       
            y += sj * (1 if self.direction[1] >= 0 else -1)
            for j in range(0, M):
                self._decorate(item, x, y)
                x += self.direction[0]
                y += self.direction[1]
        return item
                
    def _decorate(self, item, i, j):   
        if i>=0 and i < item.W and j>=0 and j < item.H:     
            if item.symbols[j,i] != '':
                item.symbols[j,i] = self.char
                item.fgcolors[j,i] = colors[self.color]
        
class Rectangle(AsciiItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._anchor = (0, 0)

    
class TriangleUp(AsciiItem):
    def __init__(self, height, fgcolor='white', char='*'):
        W = 2*height-1
        super().__init__(width=W, height=height, fgcolor=fgcolor, char='')
        self._anchor = (self.W//2, 0)
        for i in range(self.H):
            self.symbols[i, i:self.W-i] = char
      
    
class GiftBox(AsciiItem):
    def __init__(self):
        super().__init__(width=3, height=3, char='*')
        self._anchor = (1,0)
        self.fgcolors.fill(colorama.Fore.WHITE)
        self.fgcolors[:,1] = colorama.Fore.RED
        self.fgcolors[1,:] = colorama.Fore.RED

        
class Tree(AsciiItem):
    def __init__(self, crownH=10, trunkH=5, trunkW=3, decorator=lambda x : x):
        crown = TriangleUp(height=crownH, fgcolor='green', char='#')
        super().__init__(width=crown.W, height=crown.H + trunkH, char='')
        self.add(Rectangle(char='8', fgcolor='black', width=trunkW, height=trunkH), crown.anchor[0]-trunkH//2+1, 0)
        self.add(decorator(crown), (crown.W-1)//2, trunkH)
        self._anchor = crown.anchor
                
    
class AsciiWorld(AsciiItem):
    def __init__(self, width, height):
        super().__init__(width=width, height=height)
        self.symbols.fill(' ')
        self.bgcolors.fill(f"{colorama.Back.BLUE}")
        self.fgcolors.fill('')

   
    def print(self):
        for i in range(self.H-1, -1, -1):
            s=''
            for j in range(self.W):
                s+=f"{self.bgcolors[i,j]}{self.fgcolors[i,j]}{self.symbols[i,j]}"
            print(s, end='')
            print(colorama.Style.RESET_ALL, end='')
            print('',end='\n')
        print('My picture')
                
if __name__ == '__main__':
    world = AsciiWorld(80, 60)
    world.add(GiftBox(), x=25, y=0)
    chains = StripesDecorator(step=5)
    world.add(Tree(crownH=10, decorator=chains), 20, 0)
    chains.direction = (-1,1)
    world.add(Tree(crownH=10, decorator=chains), 60, 0)
    world.print()
    
