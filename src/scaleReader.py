#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Serial reader and updater
import serial

file_location = '/var/www/html/web/uploads/scale.txt'
#ser = serial.Serial('/dev/ttyUSB0',9600, timeout=10)
try:
    ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600, timeout=10,stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN)
except serial.SerialException as e:
    print("could not open serial port '{}': {}".format('lsls', e))

print(ser.name)

oldvalue = ''

while True:
    line = ser.readline()
    val1 = line[4:9]
    val2 = line[9:10]
    value = '%s.%s' % (val1, val2)

    if (value != oldvalue):
	oldvalue = value
	f = open(file_location, "w")
	f.write(value)
	f.close()
	print(value + '\n') 
    # further processing 
    # send the data somewhere else etc
ser.close()