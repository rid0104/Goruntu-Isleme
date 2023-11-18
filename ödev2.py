import cv2
import numpy as np


vid = cv2.VideoCapture(0)

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

while True:
    ret,frame = vid.read()

    cv2.imshow('frame',frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask= cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    kInp=cv2.waitKey(1)

    if kInp == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()


