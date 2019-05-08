# Intelligent drowsiness monitor for safer driving through vision.

<img src="https://i.ibb.co/C6NcYh7/Intelligent-drowsiness-monitor.png" width="1000">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [VMA Circuit for RaspberryPi](#vma-circuit-for-raspberrypi)
* [Raspberry Setup](#raspberry-setup)
* [Raspberry Software Development](#raspberry-software-development)
* [Configure the Raspberry to initialize the code with boot](#configure-the-raspberry-to-initialize-the-code-with-boot)
* [Cloud Development](#cloud-development)
* [The assembly of the product](#the-assembly-of-the-product)
* [The Final Product](#the-final-product)
* [Future Rollout](#future-rollout)
* [References](#references)

## Introduction:

Sleeping, one of the most basic needs of the human being, is a daily task that, at least, we must perform for 8 hours. However, it seems that sleeping is a luxury that not many can have. Some do not sleep for pending work, for enjoying some more episodes of their favorite series, or even for a party.

Not sleeping today is a common practice among young people, however not sleeping reduces the ability to react and attention to perform tasks as simple as sending a text message or even tasks as complex as **driving a car**.

According to the National Highway Traffic Safety Administration and the Centers for Disease Control and Prevention they say that it is 7 times dangerous driving tired to driving drunk.

- Number of drunk driving crashes: 10,874 *
- Number of tired driving crashes: 72,000 **

The problem we have here is, what happens if we need to drive and we are tired?

The best solution to this problem will always be to sleep at night, if it is not possible to do it, as a solution I create the drowsiness monitor to avoid falling asleep while driving.

https://www.nhtsa.gov/risky-driving/drunk-driving *
https://www.cdc.gov/features/dsdrowsydriving/index.html **

## Materials:

- Huawei 3G USB dongle (MS2131i)    x 1.
- Soracom Global SIM Card           x 1.                        
- Raspberry Pi 3                    x 1.
- Generic Webcam                    x 1.
- VMA204 Accelerometer              x 1.
- Little Speaker  (Generic)         x 1.
- PCB Breadboard                    x 1.
- Case                              x 1.
- Battery 5v (2.5 amps)             x 1.
- USB to Microusb cable             x 1.
- Touchpad and Keyboard USB         x 1. (https://www.amazon.com/dp/B07KZ7S6S7/ref=cm_sw_r_tw_dp_U_x_cuM0CbQZBX6VH)
- HDMI Cable                        x 1.
 
Optional to make the PCB Breadboard:

- Soldering Station.
- Wire Wrap Cable.
- Soldering Iron.
- PCB Breadboard.  

## Connection Diagram:

This is the connection diagram of the system:

<img src="https://i.ibb.co/VQTz5bN/Car.png" width="800">

## VMA Circuit for RaspberryPi:

As a first step it is necessary to make a circuit that allows the Raspberry to obtain the accelerometer data, communicated by I2C also known as TWI, it will be necessary to realize a circuit which allows the connection of this module to the headers of the raspberry.

<img src="https://i.ibb.co/z263cRP/Untitled-1.png" width="500">

This is the connection diagram:

<img src="https://i.ibb.co/k8WMrFY/VMA.png" width="500">

In my case I made a "Shield" with a PCB Breadboard so I could place it on the raspberry easily.

<img src="https://i.ibb.co/55Jb665/IMG-20190507-231237-2.jpg" height="250"><img src="https://i.ibb.co/K9PQs0Y/IMG-20190507-231304-2.jpg" height="250">

Already placed on the raspberry:

<img src="https://i.ibb.co/WpPk3HC/IMG-20190506-132743-2.jpg" height="300"><img src="https://i.ibb.co/G2HQ71m/IMG-20190506-132756-2.jpg" height="300">

Otherwise, if you do not want to make this "Shield" you can simply connect it using dupont cable XP, but the soldered circuit is always better.

## Raspberry Setup:

Note: for this tutorial it is necessary setup the raspberry with an HDMI monitor and a Touchpad and Keyboard USB, we will not use a normal internet connection, we use a connection through the Huawei 3G USB dongle, it is not advisable to use wireless.

* Download "Raspbian Stretch with desktop" from https://www.raspberrypi.org/downloads/raspbian/.
* Flash Raspbian on the sd card as indicated on the official page. https://www.raspberrypi.org/documentation/installation/installing-images/README.md
* Connect the RaspberryPi 3 HDMI cable, connect the other side of the cable to the screen.
* Connect the SD card to the raspberry.
* Connect the USB of the Touchpad and Keyboard to the raspberry.
* Comes the Huawei 3G USB dongle to the raspberry.
* Connect the speaker to the jack output of the raspberry.
* In this case connect the USB cable to the battery and the microUSB to the Raspberry for powered.
* Once you achieve this you should see Raspbian's desktop on the screen.

<img src = "https://thepi.io/wp-content/uploads/2017/10/raspberry-pi-desktop-500px.png" width = "500">  

### OpenCV Setup:

* As a first step to configure raspberry correctly we will have to connect to a Wifi network, because we will have to install OpenCV in the raspberry.

- https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/

This was the tutorial that I used and it worked, however there are many different tutorials on internet, if this does not work try another one.

- https://www.learnopencv.com/tag/raspberry-pi/
- https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/

* After performing the tutorial, we will put the following command in the terminal.

       pip install smbus pygame time
      
* With this command we will have all the libraries installed.

Example of image processing with OpenCV: Click on the image
[![OpenCV Processing](https://robologs.net/wp-content/uploads/2014/04/opencv_logo.png)](https://youtu.be/9zasymtyrO0)

### Webcam Setup:

* To install the webcam correctly we will use the following Raspberry official guide.

https://www.raspberrypi.org/documentation/usage/webcams/

* As a last step we disconnected the internet raspberry to stay only with the connection that the Soracom Dongle will give us.

### Dongle Setup:

* To configure the Dongle, we will use the official Soracom guide to correctly configure the dongle in the raspberry.

https://github.com/soracom/handson/wiki/1.3.-USB-Dongle-configuration-tutorial

## Raspberry Software Development:

Para este tutorial solo tendremos que abir el editor Thonny en la raspberry y pegar el siguiente codigo, todo el codigo esta comentado y explicado.

    # -*- coding: utf-8 -*-
    """
    Created on Thu Apr 11 01:48:57 2019

    @author: ANDRE
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
    import json
    
    # Code to create the Accelerometer Module and obtain data from its.
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
    
    #Audio File attached in the repository or hackster page
    file = 'b.mp3'  
    #Initialization of pygame to play audio.
    pygame.init()
    pygame.mixer.init()

    # The haarcascades are attached in the respository and hackster tutorial.
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

    # Input Camera Source.
    cap = cv2.VideoCapture(0)
    # Url to send data to Soracom and Obtain Location
    url = 'http://funnel.soracom.io'
    send_url = 'http://freegeoip.net/json'
    
    #Count Variables
    nf=1    #Number of Faces
    ne=1    #Number of Eyes
    count=0 #Special Counter 

    mma = MMA7455()
    
    # Memory X,Y and Z values to compare
    xmem=mma.getValueX()
    ymem=mma.getValueY()
    zmem=mma.getValueZ()
    
    #Converting signed byte values to unsigned byte
    
    if(xmem > 127):
        xmem=xmem-255
    if(ymem > 127):
        ymem=ymem-255
    if(zmem > 127):
        zmem=zmem-255
        
        
    # Seed Time values
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
           
        # We need compare the memory value and the actual value to determine the acceleration, if the acceleration is more than 10, we determine the car crash, you can adjust this value for your convenience.
      
        if(abs(xmem-x)>10):
            print('crash')
            # to obtain our location we send a request to "send_url" url to obtain our position
            r = requests.get(send_url)
            j = json.loads(r.text)
            # We convert json to string
            lat = j['latitude']
            lon = j['longitude']
            # We create the payload and headers
            payload = '{"deviceid" : "Car 0001",    "lat" : lat, "lon" :lon}'
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            # We send to soracom the notification
            r = requests.post(url, data=payload, headers=headers)
            exit()
        if(abs(ymem-y)>10):
            print('crash')
            # to obtain our location we send a request to "send_url" url to obtain our position
            r = requests.get(send_url)
            j = json.loads(r.text)
            # We convert json to string
            lat = j['latitude']
            lon = j['longitude']
            # We create the payload and headers
            payload = '{"deviceid" : "Car 0001",    "lat" : lat, "lon" :lon}'
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            # We send to soracom the notification
            r = requests.post(url, data=payload, headers=headers)
            exit()
        if(abs(zmem-z)>10):
            print('crash')
            # to obtain our location we send a request to "send_url" url to obtain our position
            r = requests.get(send_url)
            j = json.loads(r.text)
            # We convert json to string
            lat = j['latitude']
            lon = j['longitude']
            # We create the payload and headers
            payload = '{"deviceid" : "Car 0001",    "lat" : lat, "lon" :lon}'
            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            # We send to soracom the notification
            r = requests.post(url, data=payload, headers=headers)
            exit()
        
        # We obtain an image from our source of images (in this case the camera)
        ret, img = cap.read ()
        # through the following algorithm we get the number of faces and eyes that the camera can see
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
        # Since we have the number of faces we will check that the algorithm can see at least one face and at least one open eye, if it is able to see a face and does not detect any open eye, after 3 seconds it will start to sound an annoying noise that will wake up to the condutor
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
    
* Save the file in the Desktop with the name "E.py".
    
## Configure the audio and initialize the code with boot.

* Open terminal and write the next command.

      sudo nano /etc/rc.local

* Add after "fi" paste the next code to set the jack output and excecute the program.

      amixer cset numid=3 1
      sudo python E.py
      
## Cloud Development:

Note: This tutorial is designed for people who already have an account and SIM registered in https://console.soracom.io/

### Configuration AWS IAM Credentials.

As a first step we will have to configure AWS IAM so that Soracom can communicate without restrictions to AWS IoT.

* In the AWS console we look for IAM.
<img src = "https://i.ibb.co/rm6QJtG/1.png" width = "700">
* We enter the option of IAM.
<img src = "https://i.ibb.co/MMGqpmj/2.png" width = "700">
* Inside the IAM console we enter the "Users" option.
<img src = "https://i.ibb.co/25HJ2TQ/3.png" width = "700">
* Click on the "Add user" button.
<img src = "https://i.ibb.co/92S0wdg/4.png" width = "700">
* We put the name you want and select the option "Programatic Access".
<img src = "https://i.ibb.co/Y7TKB0h/5.png" width = "700">
* In the "Attach existing polices directly" option, we select "AWSIotFullAccess".
<img src = "https://i.ibb.co/gTxmPLt/6.png" width = "700">
* Once we finish everything we will access our Access key ID and Secret Access key (Save them well because we will use them to configure the Soracom console)
<img src = "https://i.ibb.co/khZfY57/7.png" width = "700">
* We go to the AWS IoT Console and go to the "Settings" option.
<img src = "https://i.ibb.co/r5FCCTm/11.png" width = "700">
* In the "Settings" option we obtain our Endpoint API.
<img src = "https://i.ibb.co/gv3p1J3/12.png" width = "700">

### Configuration Soracom Funnel.

* In the Soracom console we enter the group that is the SIM Card.
<img src = "https://i.ibb.co/ZV5m9BT/8.png" width = "700">
* Browse Funnel and paste the Endpoint that we obtained in the AWS IoT console and add the Topic where we will post the data.
<img src = "https://i.ibb.co/nfLQ421/9.png" width = "700">
* Finally We create the IAM credentials in Funnel as shown in the image.
<img src = "https://i.ibb.co/2Pr0tc2/10.png" width = "700">

### Configuration AWS SNS.

* We create the topic that we want.
<img src = "https://i.ibb.co/09fSKVr/25.png" width = "700">
<img src = "https://i.ibb.co/DzchgQY/26.png" width = "700">
* To subscribe an email or a mobile phone select the option "Create subscription"
<img src = "https://i.ibb.co/QCz6SH4/27.png" width = "700">
* All the notification options we can make are all the following.
<img src = "https://i.ibb.co/DpWqY6x/28.png" width = "700">

### Configuration AWS IoT.

* In AWS IoT we will create a rule that allows interacting with other AWS services such as Lambda.

* In AWS IoT Enter the "Act" tab
<img src = "https://i.ibb.co/W5jFB2h/13.png" width = "700">
* Click on "Create"
<img src = "https://i.ibb.co/DDgVXwW/14.png" width = "700">
* We select any name for the rule and we put in Rule Query statement

      SELECT * FROM "crash"

<img src = "https://i.ibb.co/4PJsyyL/15.png" width = "700">
* We select the option "Add action"
<img src = "https://i.ibb.co/HC5XWB7/16.png" width = "700">
* We select the option of Send message to lambda.
<img src = "https://i.ibb.co/Kmrrwfm/17.png" width = "700">
* We select "Create a new Lambda function"
<img src = "https://i.ibb.co/wBW9sT1/18.png" width = "700">
* We set the Lambda configuration as shown on the screen.
<img src = "https://i.ibb.co/GWzs3YM/19.png" width = "700">
* In the code section we paste the code below, editing the "TopicArn" for the topic created in the previous point of SNS.
<img src = "https://i.ibb.co/DD8W9FY/20.png" width = "700">

* Lambda NodeJS Code:

      console.log ('Loading function');
      // Load the AWS SDK
      var AWS = require ("aws-sdk");

      // Set up the code to call when the Lambda function is invoked
      exports.handler = (event, context, callback) => {
      // Load the message passed into the Lambda function into a JSON object
      var eventText = JSON.parse (JSON.stringify (event, null, 2));


      // Log a message to the console; You can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console

      // Create a string, extracting the click type and serial number from the message sent by the AWS IoT button

      // Write the string to the console


      var latitude = parseInt (eventText.lat)
      var longitude = parseInt (eventText.lon)


      // Create an SNS object
      var sns = new AWS.SNS ();

      console.log ("Received event:" + "https://www.google.com.mx/maps/@" + eventText.lat + "," + eventText.lon);

      var params = {
      Message: ("Your family or your employee has crashed at the following address:" + "https://www.google.com.mx/maps/@"+ eventText.lat +", "+ eventText.lon),
      TopicArn: "arn: aws: sns: ap-northeast-1: XXXXXXXXXXXX: SoracomCar" // Your SNS URL
      };
      sns.publish (params, context.done);

      };
      
* Once the lambda is created, we return to the tab "Configure Action" to add the lambda to the rule and select the lambda we created.
<img src = "https://i.ibb.co/2NsfrMm/22.png" width = "700">

* After this and everything will be working, every time you send data of a crash will be notified by SNS to all recipients of email or cell subscribed.

## The assembly of the product:

* Mount the battery in the case that we will use to power the raspberry.
<img src = "https://i.ibb.co/sRSLnCp/IMG-20190506-132701.jpg" width = "600">

* Mount the raspberry on the battery.
<img src = "https://i.ibb.co/02TjPcg/IMG-20190506-132724.jpg" width = "600">

* We connect our "Shield" of the accelerometer.
<img src = "https://i.ibb.co/SmxqNhj/IMG-20190506-132756.jpg" width = "600">

* We put our USB cable to microUSB to power the Raspberry.
<img src = "https://i.ibb.co/1dj6jPn/IMG-20190506-133112.jpg" width = "600">

* We connect our Speaker to the jack output of the raspberry.
<img src = "https://i.ibb.co/SnfSr57/IMG-20190506-133130.jpg" width = "600">

* We connect the USB camera to the Raspberry.
<img src = "https://i.ibb.co/j8rH6VJ/IMG-20190506-133252.jpg" width = "600">

* We connect the Raspberry Dongle.
<img src = "https://i.ibb.co/sHvnkTQ/IMG-20190506-133351.jpg" width = "600">

* We close the Case to finish the product.
<img src = "https://i.ibb.co/WvyNfnP/IMG-20190506-133512.jpg" width = "600">

## The Final Product:

Now just put it in your vehicle and READY! You will not have to worry about falling asleep while driving!

Video: Click on the image
[![Intelligent drowsiness monitor](https://i.ibb.co/C6NcYh7/Intelligent-drowsiness-monitor.png)](https://www.youtube.com/watch?v=Mg6gM844Tjs)

Sorry github does not allow embed videos.

## Future Rollout:

During the development of the project, I enjoy the Soracom platform to send data to AWS IoT, the next development that can be sought to follow this product is to improve the case and the components to obtain the following advantages:

- Power the RaspberryPi with a feeder in the car.
- Improve the facial and ocular recognition algorithm.
- Improve the case to make an attractive product.

## References:

All the information about the technology used, and direct references are in our wiki:

Wiki: https://github.com/altaga/

Top:

* [Table of Contents](#table-of-contents)
