import cv2
import numpy as np
def CaptureCamera():
    cap = cv2.VideoCapture(0) #카몌라 불러오기

    if cap.isOpened() == False: #카메라 열림 확인
        exit()


    ret, image = cap.read()
    cv2.imwrite('/home/pi/myTest/EncoreSecondTeamProject/Python/test2.png',image)

    cap.release()
    cv2.destroyAllWindows()

def LoadPicture():
    return cv2.imread('/home/pi/myTest/EncoreSecondTeamProject/Python/test.png',cv2.IMREAD_COLOR)
    
def GetHImage(capImg):
    blurImg = cv2.GaussianBlur(capImg, (5,5), 0)
    HSVImg = cv2.cvtColor(blurImg,cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(HSVImg)
    ret, dst = cv2.threshold(H,50,255,cv2.THRESH_BINARY)
    # cv2.imshow('H',dst)       #손가락 분리
    # cv2.waitKey(0)
    return H
def Labeling(HImage):
    edge = cv2.Canny(HImage, 50 ,150)
    image, contours, hierachy = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image = cv2.drawContours(edge, contours[0], -1, (255,0,0),1)
    # cv2.imshow("result",image)
    # cv2.waitKey(0)
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(edge)
    for i in range(nlabels):
        if i < 2:
            continue
        area = stats[i, cv2.CC_STAT_AREA]
        center_x = int(centroids[i,0])
        center_y = int(centroids[i,1])
        left = stats[i,cv2.CC_STAT_LEFT]
        top = stats[i, cv2.CC_STAT_TOP]
        width = stats[i, cv2.CC_STAT_WIDTH]
        height = stats[i, cv2.CC_STAT_HEIGHT]

        if area > 50:
            cv2.rectangle(image, (left,top),(left+width, top+height), (0,0,255),1)
            cv2.circle(image,(center_x, center_y),5,(255,0,0),1)
            cv2.putText(image, str(i), (left+20, top + 20), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("result",image)
    cv2.waitKey(0)        
def main():
    HImage = GetHImage(LoadPicture())
    Labeling(HImage)

main()