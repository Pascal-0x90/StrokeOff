#################################
#           StrokeOff           #
#          Nathan Smith         #
#  Software protection against  #
#       HID Attacks via USB     #
#################################


from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "This is some example text. this is something that could be executed within a terminal and taking over " \
            "your computer":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.01)