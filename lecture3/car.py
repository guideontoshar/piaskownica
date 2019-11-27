# -*- coding: utf-8 -*-

class Car(object):
    def __init__(self, fuel=0):
        self.fuel = fuel
        self.toy = Car()
        print('Made a car')

if __name__ == '__main__':
    c = Car()