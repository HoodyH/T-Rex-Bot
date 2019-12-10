from threading import Thread
import time
from time import sleep
import pyautogui as pg


class TimedMoves(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

        self.__timers = []

    @property
    def time(self):
        return time.time()

    def add_action(self, action, delay):
        self.__timers.append(
            (action, self.time + delay)
        )

    @staticmethod
    def up():
        pg.press("space")

    @staticmethod
    def down():
        pg.keyDown("down")
        sleep(0.03)
        pg.keyUp("down")

    def run(self):
        while not self.stopped.wait(0.002):
            try:
                el = self.__timers[0]
            except IndexError:
                el = None

            if el is not None:
                action = el[0]
                action_time = el[1]

                if self.time > action_time:
                    # print('Executing Action: {}'.format(el))
                    action()
                    self.__timers.pop(0)
                    # print('Action List: {}'.format(self.__timers))



