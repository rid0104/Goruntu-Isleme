import cv2
import numpy as np

gri=cv2.imread("pirinc2.jpg",0)
cv2.imshow("gri pirinc2",gri)

thresh= 155
ret,thresh_gri=cv2.threshold(gri,thresh,255,cv2.THRESH_BINARY)

cv2.imshow("thresh gri",thresh_gri)

contours, hierarchy = cv2.findContours(thresh_gri, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Bulunan nesne sayısı: ", len(contours))

cv2.waitKey(0)
cv2.destroyAllWindows()






