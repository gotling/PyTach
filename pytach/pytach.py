#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyTach.

Usage:
    pytach.py <device> <command> [-v]
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
"""

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import sys
import multiprocessing
from docopt import docopt

import config
import dispatch

def main():
    arguments = docopt(__doc__, version='PyTach 0.1')
    config.arguments = arguments
    jobs = []
    if len(arguments) >= 1:
        if arguments['--web']:
            import web.web as web
            web.app.run()
            sys.exit(0)

        if arguments['--arduino']:
            import arduino.arduino as arduino
            if arguments['<command>']:
                arduino.send(arguments['<command>'])
                sys.exit(0)
            else:
                #arduino.send_and_read()
                p = multiprocessing.Process(target=arduino.read)
                jobs.append(p)
                p.start()
                p.join();
                print "Arduino listener started"
                raw_input("Use keyboard interupt to exit (CTRL + C).\n")
                sys.exit(0)

        try:
            dispatch.device(arguments['<device>'], arguments['<command>']);
        except NameError, e:
            print "Input error:", e
            print "Use 'pytach.py --help' to list available devicese"
            sys.exit(0)
    else:
        print usage
        sys.exit(0)

if __name__ == '__main__':
    main()