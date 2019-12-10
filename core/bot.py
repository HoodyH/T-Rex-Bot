from threading import Event
from time import sleep
import mss
from numpy import array, mean

from core.monintors import next_obstacle_monitor
from core.moves import TimedMoves
from core.process import process_image
from core.velocity import DelayCalculation
from config import *


class RexRunner:
    def __init__(self):
        self.sct = mss.mss()

        self.stop_flag = Event()
        self.tm = TimedMoves(self.stop_flag)
        self.dc = DelayCalculation(self.stop_flag, jump_delay)

        self.obstacle_status = False
        self.obstacle_color_value = 0

        self.obstacle_time_in = 0

    @property
    def is_next_obstacle(self):
        sct_next_obstacle = array(self.sct.grab(next_obstacle_monitor))
        color_value = mean(process_image(sct_next_obstacle))
        if self.obstacle_color_value < color_value:
            self.obstacle_color_value = color_value
        return True if int(color_value) is not 0 else False

    @property
    def is_rising_edge(self):
        if self.obstacle_status is False and self.is_next_obstacle is True:
            return True
        return False

    def check_obstacle(self):

        if self.obstacle_status is not self.is_next_obstacle:
            if self.is_rising_edge:
                self.obstacle_time_in = self.tm.time
            else:
                obstacle_time = self.tm.time - self.obstacle_time_in
                delay_time = jump_delay - self.dc.delay
                if obstacle_time < 1:
                    self.tm.add_action(self.tm.up, delay_time - obstacle_time)
                    self.tm.add_action(self.tm.down, delay_time)
                    print('Points: {}, Delay: {}'.format(self.dc.points, self.dc.delay))
                    print('Jump in: {}, Down in: {}'.format(delay_time - obstacle_time, delay_time))

            self.obstacle_status = self.is_next_obstacle

    def run(self):

        countdown = 3
        while countdown > 0:
            print('Game Auto Start in: {}'.format(countdown))
            countdown -= 1
            sleep(1)
        print('GO')

        self.dc.points = 0  # reset the points
        self.tm.add_action(self.tm.up, 0)  # first jump to start the game

        while True:
            self.check_obstacle()

            """
            try:
                last_obstacle_time = self.tm.time - self.obstacle_time_in
                if last_obstacle_time > 3:
                    print('Restart The game')
                    break
            except TypeError:
                continue
            """

    def start_game(self):

        self.tm.start()  # start the TimedMoves
        self.dc.start()  # start the DelayCalculation
        # stop_flag.set()  # this will stop the thread

        self.run()
