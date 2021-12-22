"""Module for talking to the Christmas Tree"""
#pylint:disable=import-error
from gpiozero import LEDBoard
from gpiozero.tools import random_values

def initialise_tree(variable_led = True):
    """Return a led board object with the
    26 leds number 2 to 27
    :param variable_led: if true we can have variable brightness for
        twinkly LEDs
    """
    return LEDBoard(*range(2,28), pwm=variable_led)

def light_led(tree, led_no, twinkle = True):
    """
    light the led
    :param tree: An LEDBoard object
    :param led_no: integer LED identifier
    :param twinkle: if True the LED twinkles
    """
    print("lighting", led_no)
    if twinkle:
        tree.leds[led_no].source_delay = 0.1
        tree.leds[led_no].source = random_values()
    else:
        tree.leds[led_no].off()

def delight_led(tree, led_no):
    """delight the led
    :param tree: An LEDBoard object
    :param led_no: integer LED identifier
    """
    if led_no > 25:
        led_no -= 26
    print("de-lighting", led_no)
    tree.leds[led_no].off()
