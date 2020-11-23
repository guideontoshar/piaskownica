# -*- coding: utf-8 -*-

"""
Implements GUI for the Battlefield game.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


class BattleView(object):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        axcolor = 'lightgoldenrodyellow'
        axangle = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        axspeed = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
        self.angle = Slider(axangle, 'Angle', 0.1, 30, valinit=0, valstep=1)
        self.speed = Slider(axspeed, 'Speed', 0.1, 10, valinit=0)

        axfire = plt.axes([0.8, 0.025, 0.1, 0.04])
        self.firebutton = Button(axfire, 'Fire', color=axcolor, hovercolor='0.975')
        self.firebutton.on_clicked(self.start)

    def show(self):
        plt.show()

    def start(self, event):
        print('start game')


if __name__ == '__main__':
    view = BattleView()
    view.show()
