import pyautogui as pg
import time
import cv2
from mss.linux import MSS as mss
import mss.tools
from numpy import array, mean

"""
Set this data to match your configurations
"""
screen_resolution_w = 1366
screen_resolution_h = 768

# if false the browser is in the right half of the monitor
full_screen = False

"""
Use the SNAPSHOT function to match the requirements in the README
"""
top = 415
left = 830


"""

+---+                                            +---+
    ---------------------------------------------
      ___
    -__-            |
     ||             |
    ---------------------------------------------
    
    
top = 414
left = 900

You can play here http://www.trex-game.skipser.com/
Calibrate the tail of the t-rex at the start of the calibration monitor 
"""

swipe = 1

calibration_monitor = {'top': top, 'left': left, 'width': 200, 'height': 35}
down_monitor = {'top': top, 'left': left+90, 'width': 60, 'height': 35}
obstacle_monitor = {'top': top, 'left': left + 90, 'width': 90, 'height': 35}
incoming_obstacle_monitor = {'top': top, 'left': left + 90, 'width': 30, 'height': 35}


def up():
    print('jump')
    pg.press("space")


def down():
    print('crow')
    pg.press("down")


def process_image(original_image):
    # convert to gray scale
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection, this is useless for now
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def boot():

    sct = mss.mss()
    jumped = False

    speed = time.time()
    next_obstacle_speed

    while True:
        # Creates a full snapshot of the screen and returns an RGB image
        sct_obstacle = array(sct.grab(obstacle_monitor))
        sct_down = array(sct.grab(down_monitor))

        obstacle_image = process_image(sct_obstacle)

        obstacle = mean(obstacle_image)

        if int(obstacle) is not 0:
            up()
            jumped = True

        if int(obstacle) is 0 and jumped is True:
            down()
            jumped = False

        time.sleep(0.080)


def snapshot():

    with mss.mss() as sct:
        output = "sct-{top}x{left}.png".format(**calibration_monitor)
        # grub the image
        sct_img = sct.grab(calibration_monitor)
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    print('snapshot done look in root folder')


if __name__ == "__main__":
    print('Before run the bot calibrate the window with a snapshot')
    print('1 Start the BOT')
    print('2 Calibrate with a SNAPSHOT')
    print('0 or ctr-C to exit')

    while True:
        choice = int(input())

        if choice is 0:
            break

        if choice is 1:
            boot()

        if choice is 2:
            snapshot()
