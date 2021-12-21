import cv2
import time

capture = cv2.VideoCapture()
capture.open(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640,480))

for i in range(200):
    start = time.time()
    ok, frame = capture.read()
    print (ok, "Got Frame", i, " ",  time.time() - start)
    out.write(frame)
    print (ok, "Wrote Frame", i, " ",  time.time() - start)

capture.release()
out.release()


