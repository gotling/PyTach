# -*- coding: utf-8 -*-

import sys
import serial
import config
import time

import dispatch

port = '/dev/tty.usbmodemfd131'
ser = serial.Serial(port, 9600)

def send(text):
    #time.sleep(2)
    #print ser.readline()
    text += '\n'
    ser.write(text)
    print ">", text
    ser.close()

def read():
    try:
        while True:
            line = ser.readline().strip()
            print "<", line
            if (len(line.split()) == 3):
                switch, group, command = line.split()
                if switch == "device":
                    dispatch.device(group, command);
                elif switch == "activity":
                    dispatch.activity(group, command)
    except KeyboardInterrupt:
        print "Terminated by user"
    finally:
        ser.close()

def send_and_read():
    print 'Type "quit" to exit'
    #print "<", ser.readline()
    text = ""
    while text != "quit":
        text = raw_input("> ")
        ser.write(text + '\n')
        print "<", ser.readline().strip()