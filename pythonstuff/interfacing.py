#Interfacing with a thermometer exericse

#Open a serial port with the appropriate parameters

import serial
from datetime import datetime

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

#Loop so that the temperature is continuously read

while ser.isOpen():
    datastring = ser.read(size=8)
    print(datetime.utcnow().isoformat(), datastring)
