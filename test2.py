from cv2 import reduce
from matplotlib import image
from skimage.io import imread, imshow
from skimage.filters import threshold_minimum
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('insect.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh_min = threshold_minimum(image)
binary_min = image > thresh_min
dx = []
dy = []
num = 0
x = -1
y = 0
while x <= len(binary_min) - 1:
    x += 1
    if x < len(binary_min):
        for y in range(len(binary_min)):
            if binary_min[y][x] == False and not image[y][x] == 230:
                dx.append(x)
                dy.append(y)
                for _ in range(len(dx)):
                    if not abs(dx[_] - x) < 100 or abs(dy[_] - y) < 100:
                        x += 20
                        break
                    else:
                        x += 1
                    num += 1
                break
print(str(num) )
plt.imshow(image)
plt.show()

