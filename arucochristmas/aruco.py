""" Module to provide the aruco tracking logic """

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
               "aruco dictionary" : "DICT_ARUCO_ORIGINAL"
             }
    artracker = ArUcoTracker(config)

    artracker.start_tracking()

    camera=PiCamera()
    camera.resolution=(640,480)

    return artracker, camera

def get_marker_pos(artracker, camera):
    """
    Get's a single frame from the camera object, and uses the
    artracker object to detect and track an aruco tag
    """
    capture = PiRGBArray(camera)
    camera.capture(capture, format = 'bgr')
    image = capture.array
    frame = artracker.get_frame(image)
    x = None
    y = None
    ok = False
    if frame[3]:
        x = np.mean(np.array(frame[3]).flat[3::16])
        y = np.mean(np.array(frame[3]).flat[7::16]) 
    
    return ok, x, y
