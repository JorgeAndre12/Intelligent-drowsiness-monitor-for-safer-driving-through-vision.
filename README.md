# Intelligent drowsiness monitor for safer driving through vision.

<img src="https://media.giphy.com/media/2A53iheUI58rXtdvs9/giphy.gif" width="1000">

Always use technology to improve the world, if you are a black hat or gray hat hacker please abstain at this point ......... or at least leave your star to make me feel less guilty XP.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [VMA Circuit for RaspberryPi](#vma-circuit-for-raspberrypi)
* [The PCB](#the-pcb)
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

<img src="https://i.ibb.co/55Jb665/IMG-20190507-231237-2.jpg" height="300"><img src="https://i.ibb.co/K9PQs0Y/IMG-20190507-231304-2.jpg" height="300">

Already placed on the raspberry:

<img src="https://i.ibb.co/WpPk3HC/IMG-20190506-132743-2.jpg" height="300"><img src="https://i.ibb.co/G2HQ71m/IMG-20190506-132756-2.jpg" height="300">

Otherwise, if you do not want to make this "Shield" you can simply connect it using dupont cable.




The purpose of the circuit is to switch from a digital signal of 0-5 V DC to a control signal of 120 V AC.

In the first stage of the circuit we have an Infineon 600VCoolMOS C7 MOSFET, which will allow us to control the optocoupler demanding the minimum current to the Arduino board, because the optocoupler requires at least 5 volts at 36mA to be able to drive. This is very close to the limit of the current that the Arduino board can supply, however the 600VCoolMOS only requires a signal of 5 volts at 60uA, thus showing an excessive improvement in the consumption that it requires from the board.

This consumption is extremely important because it gives us the possibility of being able to literally use any controller to perform this task due to its low consumption, thus not requiring more expensive drivers that can supply said power in their ports.

<img src="https://i.ibb.co/Jx4Jbh9/Infineon.png">

The MOSFET's operation is to ground the optocoupler diode, once this is activated it allows the flow of energy through the DIAC and this in turn allows the passage of current in the TRIAC connected to the lamp and igniting it in the process.

The other great advantage of using the MOSFET is the ease of increasing the number of drivers as in image 1 or using more powerful drivers as in image 2 without changing the design of the main circuit.

<img src="https://i.ibb.co/rsnBTWZ/MOSFET1.png" width="420"><img src="https://i.ibb.co/ThJPvtG/MOSFET2.png" width="420">

Different results in different boards:

| Comparison                     | Voltage [V]  | Current [mA] | Max Current I/O Pins [mA]| Board       | Risk        |
|--------------------------------|--------------|--------------|--------------------------|-------------|-------------|
| **Without MOSFET 600VCoolMOS** | 5.0          | 15.0         | 40.0                     | Arduino UNO | LOW         | 
| **With MOSFET 600VCoolMOS**    | 5.0          | 0.06         | 40.0                     | Arduino UNO | NOTHING     |
| **Without MOSFET 600VCoolMOS** | 3.3          | 15.0         | 10.0                     | ESP32       | EXTREMELY   |
| **With MOSFET 600VCoolMOS**    | 3.3          | 0.04         | 10.0                     | ESP32       | NOTHING     |
| **Without MOSFET 600VCoolMOS** | 3.3          | 15.0         | 12.0                     | ESP8266     | HIGH        |
| **With MOSFET 600VCoolMOS**    | 3.3          | 0.04         | 12.0                     | ESP8266     | NOTHING     |

Another solution to this project would have been to use relays, which have the function of performing this same task but mechanically, by generating a "Click" on each switch. The problem with this type of component is that if we use dimerizable lights or the switching frequency was larger, the relay could not perform this task, which the mosfet, optocoupler and triac can easily do.

<img src="https://i.ibb.co/ctHj1N5/Untitled.png">

## The PCB:

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
