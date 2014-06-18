#!/usr/bin/python
# -*- coding: utf-8 -*-

"""PyTach.

Usage:
    pytach.py nexa <device> <command> [-v]
    pytach.py multibrackets <command> [-v]
    pytach.py yamaha <command> [-v]
    pytach.py epson <command> [-v]
    pytach.py --web

Options:
    --web         Start web server.
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

import os
import sys
import pickle
from docopt import docopt

import itach
import devices.nexa as nexa
import devices.multibrackets as multibrackets
import devices.yamaha_rx350 as yamaha
import devices.epson_eh_tw3200 as epson

meta_data='.pytach_settings'
arguments={}

def save_settings(cwd, dict):
    f = open(os.path.join(cwd, meta_data), 'w')
    pickle.dump(dict, f)

def load_settings(cwd):
    f = open(os.path.join(cwd, meta_data), 'r')
    return pickle.load(f)

def log(prompt, command):
    if arguments['--verbose']:
        print prompt, command

def main():
    global arguments
    arguments = docopt(__doc__, version='PyTach 0.1')
    if len(arguments) >= 1:
        if arguments['--web']:
            import web.web as web
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