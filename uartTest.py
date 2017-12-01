import serial
from time import sleep
ser = serial.Serial("/dev/ttyAMA0",9600)
time.sleep(3)
ser.write("M 2\r\n")
time.sleep(3)
ser.write("K 2\r\n")

print('serial test start ...')

def recv(serial):
	global recvData
	while True:
		recvData= serial.read(8)
		if recvData == "":
			continue
		else:
			break
		sleep(0.02)
	return recvData

try:
    while True:
        ser.write("Z\r\n")
        time.sleep(2)
       #ser.write("Hello Wrold !!!\n")
	recvData = recv(ser)
	ser.write(recvData)
        
except KeyboardInterrupt:
    if ser != None:
        ser.close()

