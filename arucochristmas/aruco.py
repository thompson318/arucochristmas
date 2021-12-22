""" Module to provide the aruco tracking logic """
#pylint:disable=import-error
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from sksurgeryarucotracker.arucotracker import ArUcoTracker


def init_camera_and_tracker():
    """
    Initialises an sksurgeryarucotracker object and
    and picamera capture object

    :returns: The initialised arucotracker and picamera objects
    """
    config = {
        "video source" : 'none',
        "debug" : False,
        "aruco dictionary" : "DICT_4X4_50"
             }
    artracker = ArUcoTracker(config)

    artracker.start_tracking()

    camera = PiCamera()
    camera.resolution = (640, 480)

    return artracker, camera

def get_marker_pos(artracker, camera):
    """
    Get's a single frame from the camera object, and uses the
    artracker object to detect and track an aruco tag
    """
    capture = PiRGBArray(camera)
    camera.capture(capture, format='bgr')
    image = capture.array
    (_port_handles, _timestamps, _framenumbers,
     tracking, _quality) = artracker.get_frame(image)
    x_ord = None
    y_ord = None
    got_frame = False
    if tracking:
        #pylint:disable=unsubscriptable-object
        x_ord = np.mean(np.array(tracking).flat[3::16])
        y_ord = np.mean(np.array(tracking).flat[7::16])
        got_frame = True

    return got_frame, x_ord, y_ord
