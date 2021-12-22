"""
An interface between skarucotracker and a raspberry pi
Christmas tree
"""
from arucochristmas.aruco import init_camera_and_tracker, get_marker_pos
from arucochristmas.christmas import initialise_tree, light_led, delight_led

tree=initialise_tree()
artracker, camera = init_camera_and_tracker()
while True:
    ok, x_ord, y_ord = get_marker_pos(artracker, camera)
    if ok:
        print ("\n[x, y] = ", x_ord, y_ord)
        light_led(tree, int(x_ord)%26)
        delight_led(tree, int(x_ord)%26 + 1)
    else:
        print('.',end='')
