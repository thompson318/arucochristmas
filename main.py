from gpiozero import LEDBoard
from gpiozero.tools import random_values

from arucochristmas.aruco import init_camera_and_tracker get_marker_pos

def light_led(tree, led_no):
    print("lighting", led_no)
    tree.leds[led_no].on()

def delight_led(tree, led_no):
    print("de-lighting", led_no)
    tree.leds[led_no].off()

if __name__ == '__main__':

    tree=LEDBoard(*range(2,28), pwm=False)    
    artracker, camera = init_camera_and_tracker()
    while True:
        ok, x,y = get_marker_pos(artracker, camera)
        if ok:
            print ("\n[x, y] = ", x, y) 
            light_led(tree, int(x)%27)
            delight_led(tree, int(x)%27 + 1)
        else:
            print('.',end='')

