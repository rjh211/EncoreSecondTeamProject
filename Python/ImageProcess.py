import cv2
import numpy as np
import sys, copy, math

def CaptureCamera():
    cap = cv2.VideoCapture(0) #카몌라 불러오기

    if cap.isOpened() == False: #카메라 열림 확인
        exit()


    ret, image = cap.read()
    cv2.imwrite('EncoreSecondTeamProject/Image_F/3.jpg',image)

    cap.release()
    cv2.destroyAllWindows()

def LoadPicture(size):
    Image =  cv2.imread('EncoreSecondTeamProject/Image_F/opnecvTest (1).jpg',cv2.IMREAD_COLOR)
    return cv2.resize(Image, dsize=size, interpolation = cv2.INTER_AREA)
    
# def GetHImage(capImg):
#     cv2.imshow("dst", capImg)
#     cv2.waitKey(0)
#     blurImg = cv2.GaussianBlur(capImg, (5,5), 0)
#     HSVImg = cv2.cvtColor(blurImg,cv2.COLOR_BGR2HSV)
#     H, S, V = cv2.split(HSVImg)
#     ret, dst = cv2.threshold(H,50,255,cv2.THRESH_BINARY)
#     return dst

# def GetFingerImg(capImg):
#     blurImg = cv2.GaussianBlur(capImg,(5,5), 0)
#     YcrcbImg = cv2.cvtColor(capImg, cv2.COLOR_BGR2YCrCb)
#     resImg = cv2.inRange(YcrcbImg,(0,133,77),(255,173,127),YcrcbImg)
#     cv2.imshow("test", resImg)
#     morpKernel = np.ones((5,5), np.uint8)
#     morpImage = cv2.dilate(resImg, morpKernel, iterations=2)
#     morpImage = cv2.erode(morpImage, morpKernel, iterations = 3)
#     morpImage = cv2.dilate(morpImage, morpKernel, iterations=1)
#     cv2.imshow("test1", morpImage)
#     cv2.waitKey(0)

    return morpImage
def BackGroundErase(capImg):
    eraseImage = cv2.inRange(capImg , (0, 100,100), (255,255,255))

    morpKernel = np.ones((5,5), np.uint8)
    morpImage = cv2.dilate(eraseImage, morpKernel, iterations=3)
    morpImage = cv2.erode(morpImage, morpKernel, iterations = 6)
    morpImage = cv2.dilate(morpImage, morpKernel, iterations=3)

    return morpImage

def Labeling(HImage):
    edge = cv2.Canny(HImage, 50 ,150)
    image, contours, hierachy = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = cv2.drawContours(edge, contours[0], -1, (255,0,0),1)
    
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(edge)
    size = [stats[i,cv2.CC_STAT_AREA] for i in range(len(stats))]
    size.sort()
    for i in range(nlabels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area == size[-2] and area >= 300:
            return area
    else: return 0

def FindFinger(cropedImage):
    colorImage = cv2.cvtColor(cropedImage.copy(), cv2.COLOR_GRAY2RGB)
    _, contours, _ = cv2.findContours(cropedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    pointOfFingerPoints = []
    for i in contours:
        hull = cv2.convexHull(i, clockwise = True)
        cv2.drawContours(colorImage, [hull], 0, (0,0,255),2)
        for j in hull:
            pointOfFingerPoints.append([j[0][0], j[0][1]])
    cv2.imshow("test",colorImage)
    cv2.waitKey(0)
    return pointOfFingerPoints

def calDistance(posX, posY):
    return int(((int(posX[0]) - int(posY[0]))**2 + (int(posX[1]) - int(posY[1]))**2)**0.5)
    
def FindFingerCount(NFP, threshold):
    PList = copy.deepcopy(NFP)
    count = 1
    # while len(NFP) != 0:
    firstNo = PList[0]
    newList = [calDistance(firstNo, i) for i in PList if int(i[1]) <= threshold]
    newList.sort()
    diffList = [newList[i+1] - newList[i] for i in range(len(newList)-1)]
    for i in diffList:
        if i>= 10 : count+=1
    return count

def FindFinger2(cropedImage):
    colorImage = cv2.cvtColor(cropedImage.copy(), cv2.COLOR_GRAY2RGB)
    _, contours, _ = cv2.findContours(cropedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt  = contours[0]

    hull = cv2.convexHull(cnt, returnPoints= False)

    defects = cv2.convexityDefects(cnt,hull)        
    l=0

    #code for finding no. of defects due to fingers
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        pt= (100,180)


            # find length of all sides of triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        s = (a+b+c)/2
        ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

        #distance between point and convex hull
        d=(2*ar)/a

        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57


        # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
        if angle <= 90 and d>30:
            l += 1
            cv2.circle(colorImage, far, 3, [255,0,0], -1)

        #draw lines around hand
        cv2.line(colorImage,start, end, [0,255,0], 2)

    cv2.imshow("colorImage", colorImage)
    cv2.waitKey(0)
    l+=1

    # pointOfFingerPoints = []
    # for i in contours:
    #     hull = cv2.convexHull(i, clockwise = True)
    #     defects= cv2.convexityDefects(i, hull)
    #     cv2.drawContours(colorImage, [hull], 0, (0,0,255),2)
    #     cv2.drawContours(colorImage, [defects], 0, (255,0,255),2)
    #     for j in hull:
    #         pointOfFingerPoints.append([j[0][0], j[0][1]])
    # cv2.imshow("test",colorImage)
    # cv2.waitKey(0)
    # return pointOfFingerPoints

def main():
    # size = tuple(map(int, input("input Size width, height : ").split()))
    size = (400, 400)
    shadowImage = BackGroundErase(LoadPicture(size))
    area = Labeling(shadowImage)
    if area == 0: print("인식 오류")
    elif 842 < area <= 1150: print("1")
    elif 1150 < area <= 1385 : print("2")
    elif 1385 < area <= 1619 : print("3")
    elif 1619 < area <= 1796 : print("4")
    elif 1796 < area : print("5")
    else : print("0")
    

main()