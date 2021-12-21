import numpy as np
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from picamera import PiCamera
from picamera.array import PiRGBArray
from sksurgeryarucotracker.arucotracker import ArUcoTracker

def get_marker_pos(tree):
    config = { "video source" : 'none', 
               "debug" : False, 
               "aruco dictionary" : "DICT_ARUCO_ORIGINAL"
             }
    tracker = ArUcoTracker(config)

    tracker.start_tracking()

    camera=PiCamera()
    camera.resolution=(640,480)
    capture = PiRGBArray(camera)

    while True:
        camera.capture(capture, format = 'bgr')
        image = capture.array
        frame = tracker.get_frame(image)
        if frame[3]:
            x = np.mean(np.array(frame[3]).flat[3::16])
            print ("\nx = ", x) 
            print ("y = ", np.mean(np.array(frame[3]).flat[7::16])) 
            light_led(tree, int(x)%27)
            delight_led(tree, int(x)%27 + 1)
        else:
            print('.',end='')


def light_led(tree, led_no):
    print("lighting", led_no)
    tree.leds[led_no].on()

def delight_led(tree, led_no):
    print("de-lighting", led_no)
    tree.leds[led_no].off()

if __name__ == '__main__':

    tree=LEDBoard(*range(2,28), pwm=False)    
    get_marker_pos(tree)

