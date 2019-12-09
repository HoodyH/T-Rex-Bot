import pyautogui as pg
import time
import cv2
from mss.linux import MSS as mss
import mss.tools
from numpy import array, mean

monitor = {'top': 414, 'left': 900, 'width': 70, 'height': 35}


def up():
    pg.press("space")
    # time.sleep(0.8)
    # pg.press("down")


def down():
    pg.press("down")


def process_image(original_image):
    # convert to gray scale
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection, this is useless for now
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def boot():

    sct = mss.mss()

    while True:
        # Creates a full snapshot of the screen and returns an RGB image
        sct_img = sct.grab(monitor)

        sct_img = array(sct_img)
        processed_image = process_image(sct_img)

        gradient = mean(processed_image)
        print('gradient = ', gradient)

        if int(gradient) is not 0:
            up()

        time.sleep(0.095)


def snapshot():

    with mss.mss() as sct:
        # The screen part to capture
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


if __name__ == "__main__":
    print('Before run the bot calibrate the window with a snapshot')
    choice = input('1) start the BOT\n2) calibrate with a SNAPSHOT\n')
    print(choice)
    if choice == '1':
        boot()

    if choice == '2':
        snapshot()
