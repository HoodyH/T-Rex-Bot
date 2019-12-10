from core.bot import RexRunner
from core.calibration import snapshot


if __name__ == "__main__":
    print('Before run the bot calibrate the window with a snapshot')
    print('1 Start the BOT')
    print('2 Calibrate with a SNAPSHOT')
    print('0 or ctr-C to exit')

    while True:
        # choice = int(input())
        choice = 1
        if choice is 0:
            break

        if choice is 1:
            rex = RexRunner()
            rex.start_game()

        if choice is 2:
            snapshot()
