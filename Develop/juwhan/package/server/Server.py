import socket
import numpy
import cv2
import io
from PIL import Image
from constant import *

    
class Server:
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.bind((UDP_IP,UDP_PORT))
        self.picture=b''
        self.data=None
        self.addr=None
        self.path=SAVE_IMAGE_PATH
        self.img_num=0
    def save_picture(self):
        
        
        image_stram=io.BytesIO(self.picture)
        image=Image.open(image_stram)
        image.show()
        image.save(self.path+self.img_num+".jpg")
        self.img_num+=1


    def recevie_data(self):
        while True:
            self.picture=b''
            while True:
                data,addr=self.socket.recvfrom(5500)
                if data == b'end':
                    break 
                self.picture+=data
            self.save_picture()

if __name__=="__main__":
    ser=Server()
    ser.recevie_data()    