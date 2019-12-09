import pyautogui as pg
import time
import cv2
from mss.linux import MSS as mss
import mss.tools
from numpy import array, mean

"""
Set this data
"""
screen_resolution_w = 1920
screen_resolution_h = 1080

top = 415
left = 830


"""
top = 414
left = 900

You can play here http://www.trex-game.skipser.com/
Calibrate the tail of the t-rex at the start of the calibration monitor 
"""

calibration_monitor = {'top': top, 'left': left, 'width': 200, 'height': 35}
pterodactylus_monitor = {'top': top + 30, 'left': left+100, 'width': 70, 'height': 5}
kaktus_monitor = {'top': top, 'left': left+90, 'width': 80, 'height': 35}


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

    while True:
        # Creates a full snapshot of the screen and returns an RGB image
        sct_kaktus = sct.grab(kaktus_monitor)
        sct_pterodactylus = sct.grab(pterodactylus_monitor)

        sct_kaktus = array(sct_kaktus)
        processed_image = process_image(sct_kaktus)

        gradient = mean(processed_image)

        if int(gradient) is not 0:
            up()
            jumped = True

        if int(gradient) is 0 and jumped is True:
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
