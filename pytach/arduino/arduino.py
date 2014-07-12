# -*- coding: utf-8 -*-

import sys
import serial
from config import config
import time

import dispatch

port = config["arduino"]["port"]
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
                elif switch == "remote":
                    if (command == "5EA19966"):
                        dispatch.activity("watch", "ps3")
                    elif (command == "5EA119E6"):
                        dispatch.activity("watch", "stop")
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