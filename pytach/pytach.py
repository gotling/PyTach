#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyTach.

Usage:
    pytach.py device <device> <command> [-v]
    pytach.py activity <activity> <command> [-v]
    pytach.py --web [-v]
    pytach.py --arduino [<command>] [-v]
    pytach.py --discover
    pytach.py --devices
    pytach.py --activities

Options:
    --web         Start web server.
    --arduino     Start Arduino serial listener or send command to Arduino.
    --discover    Look for iTach connected to the network and print status.
    -v --verbose  Print command sent and received. [default: False]
    -h --help     Show this screen.
    --devices     List available devices.
    --activities  List available activities.
    --version     Show version.
"""

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import sys
import multiprocessing
from docopt import docopt

import itach
import config
import dispatch

def list_devices():
    print "Devices:"
    for device in dispatch.devices:
        print "\t", device

def list_activities():
    print "Activities:"
    for activity in dispatch.activities:
        print "\t", activity

def web():
    import web.web as web
    web.app.run(host='0.0.0.0', debug=True)

def arduino(arguments):
    jobs = []

    import arduino.arduino as arduino
    if arguments['<command>']:
        arduino.send(arguments['<command>'])
    else:
        #arduino.send_and_read()
        p = multiprocessing.Process(target=arduino.read)
        jobs.append(p)
        p.start()
        p.join();
        print "Arduino listener started"
        raw_input("Use keyboard interupt to exit (CTRL + C).\n")

def activity_device(arguments):
    try:
        if arguments['device']:
            dispatch.device(arguments['<device>'], arguments['<command>']);
        elif arguments['activity']:
            dispatch.activity(arguments['<activity>'], arguments['<command>'])
    except NameError, e:
        print "Input error:", e
        print "Use 'pytach.py --help' to list available commands"

def main():
    arguments = docopt(__doc__, version='PyTach 0.1')
    config.arguments = arguments

    if arguments['--web']:
        web()
    elif arguments['--arduino']:
        arduino(arguments)
    elif arguments['--discover']:
        itach.discover()
    elif arguments['--devices']:
        list_devices()
    elif arguments['--activities']:
        list_activities()
    else:
        activity_device(arguments)

if __name__ == '__main__':
    main()