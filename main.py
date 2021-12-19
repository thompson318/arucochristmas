import numpy as np
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from sksurgeryarucotracker.arucotracker import ArUcoTracker

def get_marker_pos(tree):
    config = { "video source" : 0, 
               "debug" : False, 
               "aruco dictionary" : "DICT_ARUCO_ORIGINAL"
             }
    tracker = ArUcoTracker(config)

    tracker.start_tracking()

    while True:
        frame = tracker.get_frame()
        if len(frame[3]) > 0:
            x = np.mean(np.array(frame[3]).flat[3::16])
            print ("\nx = ", x) 
            print ("y = ", np.mean(np.array(frame[3]).flat[7::16])) 
            light_led(tree, int[x]%27)
            delight_led(tree, int[x]%27 + 1)
        else:
            print('.',end='')


def light_led(tree, led_no):
    tree.led[led_no].on()

def delight_led(tree, led_no):
    tree.led[led_no].on()

if __name__ == '__main__':

    tree=LEDBoard(*range(2,28), pwm=False)    
    get_marker_pos(tree)

