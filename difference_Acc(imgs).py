import cv2
import numpy as np

img1=cv2.imread("t1.jpg",0)
img2=cv2.imread("t2.jpg",0)
THRESHOLD_LIMIT = 100

ref=cv2.GaussianBlur(img1, (3,3), cv2.BORDER_DEFAULT)
test=cv2.GaussianBlur(img2, (3,3),cv2.BORDER_DEFAULT)
refG1=cv2.resize(ref,(600,500))
cv2.imshow("ref-Guassian",refG1)
testG1=cv2.resize(test,(600,500))
cv2.imshow("test-Guassian",testG1)
diff=cv2.absdiff(ref,test)
retval,thresholded = cv2.threshold(diff, THRESHOLD_LIMIT, 255, cv2.THRESH_BINARY)
# print(thresholded)

pixel_count = len(diff)*len(diff[0])
difference_score = np.sum(thresholded)*1.0 / pixel_count
y=100 - difference_score
s=round(y,2)
print(s)

i1=cv2.resize(img1,(600,500))
cv2.imshow("control", i1)

i2=cv2.resize(img2,(600,500))
cv2.imshow("query", i2)

d1=cv2.resize(diff,(600,500))
cv2.imshow("difference", d1)

t1=cv2.resize(thresholded,(600,500))
cv2.imshow("thresholded", t1)

cv2.waitKey(0)
cv2.destroyAllWindows()


# def windowSize (name,w,h,img):
#     cv2.namedWindow(name,cv2.WINDOW_AUTOSIZE)
#     cv2.resizeWindow(name,w,h)
#     cv2.imshow(name,img)


    




