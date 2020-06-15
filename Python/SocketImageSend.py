import socket
import sys
import cv2, numpy
import base64
from PIL import Image
import io

class SocketWithJava:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('192.168.137.1',9999))
    
    def RecieveFromPC(self):
        data = self.client_socket.recv(1024)
        return data

    def SendToPC(self, msg):
        self.client_socket.sendall(msg.encode())

     
    def ImageConvertBase64(self):
        # convert image to base64(string)
        with open('EncoreSecondTeamProject/Image_F/opnecvTest (1).jpg',"rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            self.client_socket.sendall(encoded_string)
        
    def Base64ConverttoImage(self):
        # convert base64 to image
        with open("test.jpg", "wb") as fh:
            fh.write(base64.decodebytes(encoded_string))
        
        frame = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
        cv2.imshow('iamge',frame)
        cv2.waitKey(0)
    def main(self):
        # self.SendToPC(sys.stdin.readline())
        # print(self.RecieveFromPC())

        self.ImageConvertBase64()

SJ = SocketWithJava()
SJ.main()