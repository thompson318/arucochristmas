import numpy as np
from sksurgeryarucotracker.arucotracker import ArUcoTracker

def get_marker_pos():
    config = { "video source" : 0, 
               "debug" : False, 
               "aruco dictionary" : "DICT_ARUCO_ORIGINAL"
             }
    tracker = ArUcoTracker(config)

    tracker.start_tracking()

    while True:
        frame = get_frame()
        if len(frame[3] > 0):
            print ("\nx = ", np.mean(np.array(frame[3]).flat[3::16])) 
            print ("\ny = ", np.mean(np.array(frame[3]).flat[7::16])) 


if __name__ == '__main__':
    get_marker_pos()

