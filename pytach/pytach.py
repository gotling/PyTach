#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyTach.

Usage:
    pytach.py nexa <device> <command> [-v]
    pytach.py multibrackets <command> [-v]
    pytach.py yamaha <command> [-v]
    pytach.py epson <command> [-v]
    pytach.py --web [-v]
    pytach.py --arduino [<command>] [-v]

Options:
    --web         Start web server.
    --arduino     Start Arduino serial listener or send command to Arduino.
    -v --verbose  Print command sent and received. [default: False]
    -h --help     Show this screen.
    --version     Show version.

Commands:
    nexa           (on | off)
    multibrackets  (up | stop | down)
    yamaha         (cd | dtv | stereo | vol_up | vol_down)
    epson          (power)
"""

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import sys
import multiprocessing
from docopt import docopt

import itach
import config
import devices.nexa as nexa
import devices.yamaha_rx350 as yamaha
import devices.epson_eh_tw3200 as epson
import devices.multibrackets as multibrackets

def log(prompt, command):
    if config.arguments['--verbose']:
        print prompt, command

def main():
    arguments = docopt(__doc__, version='PyTach 0.1')
    config.arguments = arguments
    jobs = []
    if len(arguments) >= 1:
        if arguments['--web']:
            import web.web as web
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
        elif arguments['nexa']:
            sub_command = nexa.build_command(arguments['<device>'], arguments['<command>'])
            command = itach.build_command(1, 1, sub_command, 3)
        elif arguments['multibrackets']:
            sub_command = multibrackets.get_command(arguments['<command>'])
            command = itach.build_command(1, 1, sub_command)
        elif arguments['yamaha']:
            sub_command = yamaha.get_command(arguments['<command>'])
            command = itach.build_command(1, 3, sub_command)
        elif arguments['epson']:
            sub_command = epson.get_command(arguments['<command>'])
            command = itach.build_command(1, 2, sub_command)
        else:
            print usage
            sys.exit(0)

        log(">", command)
        result = itach.send_command(command)
        log("<", result)
    else:
        print usage
        sys.exit(0)

if __name__ == '__main__':
    main()