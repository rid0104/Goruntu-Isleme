
import cv2

import numpy as np
from matplotlib import pyplot as plt
renkli=cv2.imread("landscape.jpg")


gri=cv2.imread("landscape.jpg",0)

cv2.imshow("gri manzara",gri)

cv2.waitKey(0)

img = cv2.imread('landscape.jpg', cv2.IMREAD_GRAYSCALE)

histogram = np.zeros(256)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i,j]
        histogram[pixel] += 1


plt.figure()
plt.title(" Manzara Fotografının Gri  Histogramı")
plt.xlabel("Piksel Değerleri")
plt.ylabel("Frekans")

plt.plot(histogram)

plt.show()
