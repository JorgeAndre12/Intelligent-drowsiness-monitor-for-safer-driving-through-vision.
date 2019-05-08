# Intelligent drowsiness monitor for safer driving through vision.

<img src="https://media.giphy.com/media/2A53iheUI58rXtdvs9/giphy.gif" width="1000">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [VMA Circuit for RaspberryPi](#vma-circuit-for-raspberrypi)
* [Raspberry Setup](#raspberry-setup)
* [Connect the rest of the components](#connect-the-rest-of-the-components)
* [Development](#development)
* [The Final Product](#the-final-product)
* [Comments](#comments)
* [References](#references)

## Introduction:

Sleeping, one of the most basic needs of the human, daily is a task that at least we must perform for 8 hours, in order to have energy to carry out our activities, however today it seems to be a luxury that not many they can enjoy, some do not sleep for work, for enjoying a few more chapters of their favorite series, or even for partying.

Not sleeping today is a common practice among young people, however not sleeping reduces the ability to react and attention to perform tasks as simple as sending a text message or even tasks as complex as driving a car.

The problem we have here is, what happens if we need to drive and we are tired?

According to the National Highway Traffic Safety Administration and the Centers for Disease Control and Prevention they say that it is 7 times dangerous driving tired to driving drunk.

- Number of drunk driving crashes: 10,874
- Number of tired driving crashes: 72,000

The best solution to this problem will always be to sleep at night, if it is not possible to do it, as a solution I create the drowsiness monitor to avoid falling asleep while driving.

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
 
Optional to make the PCB:

- Soldering Station.
- Wire Wrap Cable.
- Soldering Iron.
- PCB Breadboard.                   

## VMA Circuit for RaspberryPi:

As one of the first steps to realize our system, it is necessary to realize a circuit which allows the Raspberry to obey the accelerometer data, since this is communicated by I2C also known as TWI, it will be necessary to realize a circuit which allows the simple connection of this module to the headers of the raspberry.

<img src="https://i.ibb.co/z263cRP/Untitled-1.png" width="500">

In the case of the connections for the module, they would be the following:

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
* In this case connect the USB cable to the battery and the microUSB to the Raspberry for powered.
* Once you achieve this you should see Raspbian's desktop on the screen.

<img src = "https://thepi.io/wp-content/uploads/2017/10/raspberry-pi-desktop-500px.png" width = "500">  

### OpenCV Setup:

* As a first step to configure raspberry correctly we will have to connect to a Wifi network, because we will have to install OpenCV in the raspberry.

- https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/

This was the tutorial that I used and it worked, however there are many different tutorials in the network, if this does not work try another one.

- https://www.learnopencv.com/tag/raspberry-pi/
- https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/

### Dongle Setup:

* En el caso de la configuracion del Dongle utilizaremos la guia onficial de Soracom para configurar correctamente el dongle en la raspberry.

# Connect the rest of the components.

For this project it is possible to make individual modules to be able to expand the number of bulbs or high voltage devices connected to the Arduino or to any other board.

<img src="https://i.ibb.co/CbdGKS9/1module.png">

You can also make a complete module for 4 AC outputs this in order to integrate the entire system on one PCB, both files are in the "PBC Files" folder in the Github.

<img src="https://i.ibb.co/tZhy2tC/4modules.png">

## Development:

To develop this circuit, we first tested each of the stages were carried out to demonstrate its effectiveness, the first circuit to be tested was the control of the bulbs by means of a button and safety gloves due to high voltage. (Please if you are to replicate the experiment use any safety measures possible, playing with live current is not wise).

[![Test Circuit #1](https://i.ibb.co/MGxsBNS/descarga.png)](https://youtu.be/uqsgAZPN9SU)

For the second circuit since the Lamp control works well, a platform with LEDs was made to see how the Arduino controlled the lights to the rhythm of the music, the code is in the "Arduino Code" folder, the code is thoroughly commented.

[![Test Circuit #2](https://i.ibb.co/0BhfRg8/descarga-1.png)](https://youtu.be/uK5E9QZavhg)

Once we saw that the lights control worked, we connected all the components of the whole circuit in a protoboard, to control the 4 lights and connected it to the Arduino.

[![Test Circuit #3](https://i.ibb.co/28DCBnW/descarga-2.png)](https://youtu.be/EiSSqIL-sus)

As you can see this was done in steps to manage safety, I repeat it is dangerous managing live 120V AC power so take any precautions into consideration.

## The Final Product:

With the circuit running, we decided to make control modules like the one shown in the image to not depend on any cable failing in the breadboard.

<img src="https://i.ibb.co/cwBmGVz/Whats-App-Image-2019-01-10-at-17-50-41.jpg" width="300"><img src="https://i.ibb.co/JmDS6tv/Whats-App-Image-2019-01-10-at-17-59-32.jpg" width="300">

The board was made based on the one that is in the folder "PCB Files" however since we did not have transfer paper we had to make the vias with a sharpie. It is a permanenr marker so when you dip the plate in ferric chloride it survives, this process is the classic one for making homemade PCBs. You can get to know more about this process in the following link:

https://www.hackster.io/Junezriyaz/how-to-make-pcb-using-marker-531087 

After making three aditional PCB's, we decided to put the entire circuit in a box, covering it and with 4 identical lamps so that this was a more aesthetic product and easy to transport.

<img src="https://i.ibb.co/3Yjs6Qz/IMG-1415.jpg">

And we are done! With this we have finished the light synchronization system for electrical elements (120 or 220 volts).

Video: Click on the image
[![MOSMusic - The Gray Hat - Arduino Music](https://i.ibb.co/cCkXrhZ/1219145071.jpg)](https://www.youtube.com/watch?v=daAjffZg2-g)

Sorry github does not allow embed videos.

## Comments:

This project was carried out in order to demonstrate that the control of lights through microcontrollers can be efficient and cheap, since current systems at a much lower quality are sold at excessive prices and therefore not available to all.

And to showcase a creative and seldom seen approach to use the CoolMOS C7 MOSFETs provided by Infineon

## References:

All the information about the technology used, and direct references are in our wiki:

Wiki: https://github.com/altaga/MOSMusic-MM-/wiki

Top:

* [Table of Contents](#table-of-contents)
