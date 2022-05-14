import cv2
import os

yol=os.path.join(os.getcwd(),"images","chp2","elmalar3.jpg")
# yol=os.path.join(os.getcwd(),"images","chp2","sekil_geo.jpg")
# yol=os.path.join(os.getcwd(),"images","chp2","rice_1.jpg")
image = cv2.imread(yol)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
g = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
edge = cv2.Canny(g, 140, 210)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)

cv2.imshow("image",image)
cv2.waitKey(0)