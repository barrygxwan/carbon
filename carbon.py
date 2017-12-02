# -*- coding: utf-8 -*-
#Python progam to run a Cozir Sensor
from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random
import serial
import time
import datetime
#import regression
sleep_time = 5
ser = serial.Serial(
port = "/dev/ttyAMA0",
baudrate = 9600,
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 1,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout=0
)
print("Python progam to run a Cozir Sensor\n")
ser.write("M 6\r\n") # set display mode to show only CO2
ser.write("K 1\r\n") # set  operating mode
# K sets the mode,  2 sets streaming instantaneous CO2 output
# \r\n is CR and LF
ser.flushInput()

time.sleep(3)

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "376646"

# The Write API Key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "0MXP7FIPK71S3URS"

# The Hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any Username.
mqttUsername = "CO2-SENSOR-CLIENT"

# Your MQTT API Key from Account > My Profile.
mqttAPIKey ="EYHXYYPPFG22J1T7"

# Set the transport mode to WebSockets.
tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey
time.sleep(10)
lastnumber=''
while True:
   #caijizhouqi
    time.sleep(0.2)
    #ser.write("Z\r\n")
    #buffer jadgement to recv correct data
    if ser.read()is 'Z':
	 resp = ser.read(7)
    
  	 fltCo2 = resp
      	 number=int(fltCo2)*100
	 number = '%d'%number
 
    	 print(datetime.datetime.now().strftime("%H:%M"))
    #print "CO2 PPM = ", fltCo2 * multiplier
    	 print("CO2 PPM = ", number )
    
   
    	 payload = "field1=" +number


    # attempt to publish this data to the topic.
    	 try:
        	publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
	#print (" Published CPU =",cpuPercent," RAM =", ramPercent," to host: " , mqttHost , " clientID= " , clientID)

    	 except (KeyboardInterrupt):
        	break
   # temp = '\t'.join((int(datetime.datetime.now().strftime("%H%M")),number))
   # with open('result.txt','a') as f:
    #    f.write(temp + '\n')
    
    #regression.main()
   	 time.sleep(sleep_time)


