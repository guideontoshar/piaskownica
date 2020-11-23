# -*- coding: utf-8 -*-
"""
Implements GUI for the Battlefield game.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib
from matplotlib.animation import FuncAnimation

gravity = 9.81


class Projectile(object):
    verts = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0,1.0]], dtype='float')

    def __init__(self, ax, position=(0.0, 0.0), velocity=(0.0, 0.0), scale=1.0):
        self.ax = ax
        self.position = np.asarray(position, dtype='float')
        self.velocity = np.asarray(velocity, dtype='float')
        self.glyph = matplotlib.patches.Polygon(self.verts*scale, animated=True)
        self.init_verts = self.verts*scale
        self.ax.add_patch(self.glyph)
        self.time = 0
        self.step = 0

    def set(self, position, velocity):
        self.position = np.asarray(position, dtype='float')
        self.velocity = np.asarray(velocity, dtype='float')

    def draw(self):
        xy = self.init_verts + self.position
        self.glyph.set_xy(xy)

    def update(self, time):
        dt = time - self.time
        if self.position[1] >= 0.0:
            self.position += self.velocity * dt
            self.velocity += np.asarray([0.0, -gravity])*dt
            self.draw()
        self.time = time
        self.step += 1
        # print(f"step: {self.step}, time: {time}, position: {self.position}")


class BattleView(object):
    angle_limit = 90
    speed_limit = 10
    resolution = 100

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        axcolor = 'lightgoldenrodyellow'

        bbox = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        self.angle_slider = Slider(bbox, 'Angle', 0, 90, valinit=0, valstep=1)
        self.angle_slider.on_changed(self.on_update_canon)

        bbox = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
        self.speed_slider = Slider(bbox, 'Speed', 0, 10, valinit=0)
        self.speed_slider.on_changed(self.on_update_canon)

        bbox = plt.axes([0.8, 0.025, 0.1, 0.04])
        self.fire_button = Button(bbox, 'Fire', color=axcolor, hovercolor='0.975')
        self.fire_button.on_clicked(self.on_fire)

        bbox = plt.axes([0.1, 0.025, 0.1, 0.04])
        self.reset_button = Button(bbox, 'Reset', color=axcolor, hovercolor='0.975')
        self.reset_button.on_clicked(self.on_reset)

        self.projectile = None
        self.animator = None
        self.max_range = 0
        self.max_time = 0
        self.max_altitude = 0
        self.time_limit = 0
        self.range_limit = 0
        self.altitude_limit = 0
        self.time = 0.0
        self.dt = 0.0

        self.shooting = False

        self.setup_limits()
        self.draw_max_trajectory()
        self.on_reset(True)

    @property
    def angle(self):
        return self.angle_slider.val

    @property
    def speed(self):
        return self.speed_slider.val

    def setup_limits(self):
        margin_factor = 1.05
        self.time_limit = self.speed_limit*math.sqrt(2)/gravity
        self.altitude_limit = margin_factor * self.speed_limit**2/(gravity*2)
        self.range_limit = margin_factor * self.speed_limit ** 2 / gravity
        self.dt = self.time_limit/self.resolution
        self.ax.set_xlim(0.0, self.range_limit)
        self.ax.set_ylim(0.0, self.altitude_limit)

    def update_range(self):
        self.max_range = self.speed**2/gravity
        self.max_time = self.speed*math.sqrt(2)/gravity
        angle = np.radians(self.angle)
        self.max_altitude = self.speed*math.sin(angle)/gravity
        self.dt = self.max_time/self.resolution

    def draw_trajectory(self, start_time, end_time, speed, angle):
        timesteps = np.linspace(start_time, end_time, int((end_time-start_time)/self.dt))
        angle = np.radians(angle)
        x = timesteps * speed * math.cos(angle)
        y = timesteps * speed * math.sin(angle) - gravity * timesteps**2 / 2.0
        trajectory = self.ax.plot(x, y, 'b-')
        return trajectory

    def draw_max_trajectory(self):
        self.draw_trajectory(0, self.time_limit, self.speed_limit, 45)

    def on_reset(self, event):
        scale = self.range_limit / 50
        self.projectile = Projectile(self.ax, position=(0.0, 0.0), velocity=(0.0, 0.0), scale=scale)
        self.time = 0.0
        self.shooting = False

    def on_update_canon(self, _val):
        self.update_range()

    def on_fire(self, event):
        angle = np.radians(self.angle)
        vx = self.speed * math.cos(angle)
        vy = self.speed * math.sin(angle)
        self.projectile.set((0.0, 0.0), (vx, vy))
        self.shooting = True

    def on_update(self, time):
        if self.shooting:
            self.projectile.update(self.time)
            self.time += self.dt
        return self.projectile.glyph,

    def show(self):
        self.animator = FuncAnimation(self.fig, self.on_update, blit=True, interval=100)
        plt.show()


if __name__ == '__main__':
    view = BattleView()
    view.show()
