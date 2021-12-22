"""Module for talking to the Christmas Tree"""
#pylint:disable=import-error
from gpiozero import LEDBoard
from gpiozero.tools import random_values

def initialise_tree():
    """Return a led board object with the
    26 leds number 2 to 27
    """
    return tree=LEDBoard(*range(2,28), pwm=False)

def light_led(tree, led_no):
    print("lighting", led_no)
    tree.leds[led_no].on()

def delight_led(tree, led_no):
    print("de-lighting", led_no)
    tree.leds[led_no].off()
