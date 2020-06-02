import cv2
import numpy as np
def CaptureCamera():
    cap = cv2.VideoCapture(0) #카몌라 불러오기

    if cap.isOpened() == False: #카메라 열림 확인
        exit()


    ret, image = cap.read()
    cv2.imwrite('EncoreSecondTeamProject/Image_F/3.jpg',image)

    cap.release()
    cv2.destroyAllWindows()

def LoadPicture():
    return cv2.imread('EncoreSecondTeamProject/Image_F/5.jpg',cv2.IMREAD_COLOR)
    
def GetHImage(capImg):
    blurImg = cv2.GaussianBlur(capImg, (5,5), 0)
    HSVImg = cv2.cvtColor(blurImg,cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(HSVImg)
    ret, dst = cv2.threshold(H,50,255,cv2.THRESH_BINARY)
    return dst

def GetFingerImg(capImg):
    blurImg = cv2.GaussianBlur(capImg,(5,5), 0)
    YcrcbImg = cv2.cvtColor(capImg, cv2.COLOR_BGR2YCrCb)
    resImg = cv2.inRange(YcrcbImg,(0,133,77),(255,173,127),YcrcbImg)
    morpKernel = np.ones((5,5), np.uint8)
    
    morpImage = cv2.dilate(resImg, morpKernel, iterations=2)
    morpImage = cv2.erode(morpImage, morpKernel, iterations = 3)
    morpImage = cv2.dilate(morpImage, morpKernel, iterations=1)

    return morpImage

def Labeling(HImage):
    edge = cv2.Canny(HImage, 50 ,150)
    image, contours, hierachy = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = cv2.drawContours(edge, contours[0], -1, (255,0,0),1)
    
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(edge)
    size = [stats[i,cv2.CC_STAT_AREA] for i in range(len(stats))]
    size.sort()
    for i in range(nlabels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area == size[-2]:
            center_x = int(centroids[i,0])
            center_y = int(centroids[i,1])
            left = stats[i,cv2.CC_STAT_LEFT]
            top = stats[i, cv2.CC_STAT_TOP]
            width = stats[i, cv2.CC_STAT_WIDTH]
            height = stats[i, cv2.CC_STAT_HEIGHT]

            if area > 50:
                colorImg = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                cv2.rectangle(colorImg, (left,top),(left+width, top+height), (255,255,0),1)
                cv2.putText(colorImg, str(i), (left+20, top + 20), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            return HImage[top:top+height,left:left+width]
    else: return None

def FindFinger(cropedImage):
    colorImage = cv2.cvtColor(cropedImage.copy(), cv2.COLOR_GRAY2RGB)
    # grayImage = cv2.cvtColor(cropedImage, cv2.COLOR_RGB2GRAY)
    _, contours, _ = cv2.findContours(cropedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    distFromHull = []
    for i in contours:
        hull = cv2.convexHull(i, clockwise = True)
        cv2.drawContours(colorImage, [hull], 0, (0,0,255),2)
        print(hull[0][0][0], hull[0][0][1])
        # for j from len(hull[0]):
        #     distFromHull.append(calDistance(hull[0][j]))
    cv2.imshow("test",colorImage)
    cv2.waitKey(0)
def calDistance(posX, posY):
    diffX, diffY = abs(posX[0] - posY[0]), abs(posX[1] - posY[1])
    if posX[0] == posY[0]: return diffY
    elif posX[1] == posY[0] : return diffX
    else: return int(diffX/diffY)
def main():
    # HImage = GetHImage(LoadPicture())
    FingerImg = GetFingerImg(LoadPicture())
    cropedFingerImage = Labeling(FingerImg)
    # if cropedFingerImage == None:
    #     print('손가락 인식 오류')
    #     return

    FindFinger(cropedFingerImage)

main()