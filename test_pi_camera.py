import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
capture = PiRGBArray(camera)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640,480))

for i in range(200):
    start = time.time()
    camera.capture(capture, format="bgr")
    frame = capture.array
    print (ok, "Got Frame", i, " ",  time.time() - start)
    out.write(frame)
    print (ok, "Wrote Frame", i, " ",  time.time() - start)

capture.release()
out.release()


