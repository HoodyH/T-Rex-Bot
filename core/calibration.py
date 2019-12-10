import mss
from core.monintors import *


def snapshot():

    with mss.mss() as sct:
        output = 'imgs\calibration.png'
        # output = 'imgs\sct-{top}x{left}.png'.format(**calibration_monitor)
        # grub the image
        sct_img = sct.grab(next_obstacle_monitor)
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    print('snapshot done look in root folder')
