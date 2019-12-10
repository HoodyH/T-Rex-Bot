from threading import Thread
from time import sleep


class DelayCalculation(Thread):
    def __init__(self, event, max_delay):
        Thread.__init__(self)
        self.stopped = event

        self.__max_delay = max_delay
        self.__points = 0

    @property
    def max_delay(self):
        return self.__max_delay

    @max_delay.setter
    def max_delay(self, value):
        self.__max_delay = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = value

    @property
    def delay(self):
        return self.remap_range(self.__points, 0, 9999, 0, self.__max_delay)

    @staticmethod
    def remap_range(value, actual_min, actual_max, new_min, new_max):
        actual_span = actual_max - actual_min
        new_span = new_max - new_min
        value_scaled = float(value - actual_min) / float(actual_span)
        return new_min + (value_scaled * new_span)

    def run(self):
        while not self.stopped.wait(0.08):
            self.__points += 1
