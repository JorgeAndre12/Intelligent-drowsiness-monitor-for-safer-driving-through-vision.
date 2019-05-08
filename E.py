# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:48:57 2019

@author: VAI
"""
import smbus
import numpy as np
import urllib.request
import cv2
import pygame
import time
import os
import math
import requests

class MMA7455():
    bus = smbus.SMBus(1)
    def __init__(self):
        self.bus.write_byte_data(0x1D, 0x16, 0x55) # Setup the Mode
        self.bus.write_byte_data(0x1D, 0x10, 0) # Calibrate
        self.bus.write_byte_data(0x1D, 0x11, 0) # Calibrate
        self.bus.write_byte_data(0x1D, 0x12, 0) # Calibrate
        self.bus.write_byte_data(0x1D, 0x13, 0) # Calibrate
        self.bus.write_byte_data(0x1D, 0x14, 0) # Calibrate
        self.bus.write_byte_data(0x1D, 0x15, 0) # Calibrate
    def getValueX(self):
        return self.bus.read_byte_data(0x1D, 0x06)
    def getValueY(self):
        return self.bus.read_byte_data(0x1D, 0x07)
    def getValueZ(self):
        return self.bus.read_byte_data(0x1D, 0x08)

file = 'b.mp3'
pygame.init()
pygame.mixer.init()

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascade

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')


cap = cv2.VideoCapture(0)
url = 'http://funnel.soracom.io'
payload = '{"deviceid" : "Car 0001",    "lat" : 19.635, "lon" : -99.276}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


nf=1
ne=1
count=0

mma = MMA7455()

xmem=mma.getValueX()
ymem=mma.getValueY()
zmem=mma.getValueZ()
if(xmem > 127):
    xmem=xmem-255
if(ymem > 127):
    ymem=ymem-255
if(zmem > 127):
    zmem=zmem-255
    
time1=time.time()
time2=time.time()

while 1:
    
    x = mma.getValueX()
    y = mma.getValueY()
    z = mma.getValueZ()
    if(x > 127):
       x=x-255
    if(y > 127):
       y=y-255
    if(z > 127):
       z=z-255
    if(abs(xmem-x)>10):
        print('crash')
        r = requests.post(url, data=payload, headers=headers)
        exit()
    if(abs(ymem-y)>10):
        print('crash')
        r = requests.post(url, data=payload, headers=headers)
        exit()
    if(abs(zmem-z)>10):
        print('crash')
        r = requests.post(url, data=payload, headers=headers)
        exit()
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3, 40)
        ne=len(eyes)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    nf=len(faces)
    if(nf>0 and ne<1):
       time1=time.time()
       print(time1-time2)
       if((time1-time2)>=3):
           pygame.mixer.music.load(file)
           pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()
        time1=time.time()
        time2=time1
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cv2.destroyAllWindows()