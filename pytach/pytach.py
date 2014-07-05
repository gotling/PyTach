#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyTach.

Usage:
    pytach.py device <device> <command> [-v]
    pytach.py activity <activity> <command> [-v]
    pytach.py --web [-v]
    pytach.py --arduino [<command>] [-v]

Options:
    --web         Start web server.
    --arduino     Start Arduino serial listener or send command to Arduino.
    -v --verbose  Print command sent and received. [default: False]
    -h --help     Show this screen.
    --version     Show version.

Devices:
    nexa           (1:on | 1:off)
    multibrackets  (up | stop | down)
    yamaha         (cd | dtv | stereo | vol_up | vol_down)
    epson          (power)

Activities:
    watch          (ps3 | stop)
"""

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import sys
import multiprocessing
from docopt import docopt

import config
import dispatch

def web():
    import web.web as web
    web.app.run()

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
    else:
        activity_device(arguments)

if __name__ == '__main__':
    main()