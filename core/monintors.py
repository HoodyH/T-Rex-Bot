from config import *


"""

+---+                                            +---+
    ---------------------------------------------
      ___
    -__-            |
     ||             |
    ---------------------------------------------

1920/2 960
960/2 480

"""

spacer_h = int(screen_resolution_h/4 + screen_resolution_h/8)

if full_screen:
    spacer_w = int(screen_resolution_w / 8)
else:
    spacer_w = int(screen_resolution_w/2 + screen_resolution_w/8)

print('Initial position: {}h {}w'.format(spacer_h, spacer_w))

top = spacer_h + vertical
left = spacer_w + horizontal

calibration_monitor = {
    'top': top,
    'left': left,
    'width': 200,
    'height': 35
}
next_obstacle_monitor = {
    'top': top,
    'left': left + 300,
    'width': 80,
    'height': 35
}
