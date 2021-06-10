
import PIL
import cv2
import numpy as np
import urllib.request
from PIL import Image
# from skimage.metrics import structural_similarity as ssim
# from SSIM_PIL import compare_ssim

ref_count=0
test_count=0
diff_count=0
k = cv2.waitKey(1)
THRESHOLD_LIMIT = 100

url='http://192.168.1.127:8080/shot.jpg'
cam=cv2.VideoCapture(url)
ref_count=0
test_count=0


# def windowSize (name,w,h,img):
#     cv2.namedWindow(name,cv2.WINDOW_AUTOSIZE)
#     cv2.resizeWindow(name,w,h)
#     cv2.imshow(name,img)

    
def ImageCapture():
    ref_count=0
    test_count=0

    while True:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
        frame=cv2.imdecode(imgNp,-1)
        frame1=cv2.resize(frame,(550,650))
        cv2.imshow("IP Cam",frame1)
        # windowSize("Reference Win",800,700,frame)

        k = cv2.waitKey(1)
        
        if k%256 == 27:   #Escape key
            #ESC pressed
            print("Escape hit, closing...")
            break    
    
        elif k%256 == 114:  #r key
            ref_count+=1
            Reference_Image = ("Reference.png")
            cv2.imwrite(Reference_Image, frame)
            print("{} written!".format(Reference_Image))
            
        
        elif k%256==116:  #key't'
            Test_Image = ("Test_{}.png".format(test_count))
            cv2.imwrite(Test_Image, frame)
            print("{} written!".format(Test_Image))
            test_count+=1
            difference()
            
    cam.release()
    cv2.destroyAllWindows()

def difference():
    
    testImage=cv2.imread("Test_{}.png".format(test_count))
    test=cv2.cvtColor(testImage,cv2.COLOR_BGR2GRAY)
    testImage1=cv2.resize(test,(550,650))
    cv2.imshow("Query Image",testImage1)
    # windowSize("Test Win",800,700,test)

    refImage=cv2.imread("Reference.png")
    ref=cv2.cvtColor(refImage,cv2.COLOR_BGR2GRAY)
    refImage1=cv2.resize(ref,(550,650))
    cv2.imshow("Control Image",refImage1)

    # windowSize("Reference Win",800,700,ref)

    refblur = cv2.GaussianBlur(ref, (3,3), cv2.BORDER_DEFAULT)
    testblur = cv2.GaussianBlur(test, (3,3), cv2.BORDER_DEFAULT)
    # refcanny = cv2.Canny(refblur, 100, 150)
    # testcanny = cv2.Canny(testblur, 100, 150)

    # refG1=cv2.resize(refblur,(550,650))
    # cv2.imshow("ref-Guassian",refG1)
    # testG1=cv2.resize(testblur,(550,650))
    # cv2.imshow("test-Guassian",testG1)
    
    diff=cv2.absdiff(refblur,testblur)
    diff1=cv2.resize(diff,(550,650))
    cv2.imshow("Difference", diff1)
    
    retval,thresholded = cv2.threshold(diff, THRESHOLD_LIMIT, 255, cv2.THRESH_BINARY)

    pixel_count = len(diff)*len(diff[0])
    difference_score = np.sum(thresholded)*1.0 / pixel_count
    y=100 - difference_score
    s=round(y,2)
    print(s)

    t1=cv2.resize(thresholded,(550,650))
    cv2.imshow("thresholded", t1)

    # windowSize("Diff Win",600,700,diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ImageCapture()



