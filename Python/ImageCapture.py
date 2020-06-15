import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    exit()
    
while True:

    ret, img = cap.read()
    cv2.imshow('preview', img) 
   
    if cv2.waitKey(10) == ord('q'):    #q버튼을 눌렀을 때 작동.
        print('capture')
        cv2.IMREAD_UNCHANGED       
        cv2.imwrite("EncoreSecondTeamProject/Image_F/cap.png", img)   #영상캡쳐파일을 cap.png로 저장
         
    if cv2.waitKey(10) == 27:              #esc키 누르면 종료
        break
    
cap.release()
cv2.destroyAllWindows()


