# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:06:08 2020

@author: putanowr
"""
import colorama

class ChristmasTree(object):
    def __init__(self, crownH, trunkH, trunkW=3):
        self.crownH = crownH
        self.trunkH = trunkH
        self.trunkW = trunkW
        self.black_background = False
        
    def __str__(self):
        crownW = 2*self.crownH-1
        spaceW = (crownW-1)//2
        repr="" 
        repr += f"{colorama.Fore.GREEN}"
        for i in range(self.crownH):
            repr += ' '*(spaceW-i)
            repr += '*'*(2*i+1)
            repr += '\n'
        if self.black_background:
        	repr += f"{colorama.Fore.WHITE}"
        else:
        	repr += f"{colorama.Fore.BLACK}"
        for i in range(self.trunkH):
            repr += ' '*((crownW-self.trunkW)//2)
            repr += '*'*self.trunkW
            repr += '\n'
        return repr    
                
if __name__ == '__main__':
    ct = ChristmasTree(20, 7, 5)
    ct.black_background = True
    print(ct)
