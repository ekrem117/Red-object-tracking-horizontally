# Red-object-tracking-horizontally

import cv2
import numpy as np


videom = cv2.VideoCapture(0)

videom.set(3, 480)
videom.set(4,320)

ret, frame = videom.read()
row, col, _ = frame.shape

x_mid = int(col / 2)
center = int(col / 2)
position = 90

while True:
    ret, frame = videom.read()
    hsv_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x:cv2.contourArea(x), reverse=True)

    for ekrem in contours:
        (x, y, w, h) = cv2.boundingRect(ekrem)

        x_mid = int((x + x + w)/2)
        break

    cv2.line(frame, (x_mid, 0), (x_mid, 480), (0, 255, 0), 2)

    cv2.imshow("frammesss", frame)

    keyInp = cv2.waitKey(1)

    if keyInp == ord("q"):
        break
videom.release()
cv2.destroyAllWindows()
