#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import os
import sys
import pickle
import itach
import devices.nexa as nexa
import devices.multibrackets as multibrackets
import devices.yamaha_rx350 as yamaha

meta_data='.pytach_settings'

def save_settings(cwd, dict):
    f = open(os.path.join(cwd, meta_data), 'w')
    pickle.dump(dict, f)

def load_settings(cwd):
    f = open(os.path.join(cwd, meta_data), 'r')
    return pickle.load(f)

usage = """
pytach [nexa|multibrackets|yamaha] [command]
"""

def main():
    args = sys.argv
    if len(args) > 1:
        if args[1] == 'nexa':
            sub_command = nexa.build_command(args[2], args[3])
            command = itach.build_command(1, 1, sub_command)
        elif args[1] == 'multibrackets':
            sub_command = multibrackets.get_command(args[2])
            command = itach.build_command(1, 1, sub_command)
        elif args[1] == 'yamaha':
            sub_command = yamaha.get_command(args[2])
            command = itach.build_command(1, 3, sub_command)
        else:
            print usage
            sys.exit(0)

        print ">", command
        result = itach.send_command(command)
        print "<", result
    else:
        print usage
        sys.exit(0)

if __name__ == '__main__':
    main()