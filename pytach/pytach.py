#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="gotling"
__date__ ="$Jun 15, 2014 09:09:38 PM$"

import os
import sys; print sys.path
import socket
import pickle
import devices.nexa as nexa
import devices.multibrackets as multibrackets
import devices.yamaha_rx350 as yamaha

meta_data='.pytach_settings'
HOST = "192.168.0.22"
PORT = 4998
repeat = 3
timeout = 2000
module = 1
connection = 1
base_command = "sendir,[MODULE]:[CONNECTION],1,38000,[REPEAT],";

def save_settings(cwd, dict):
    f = open(os.path.join(cwd, meta_data), 'w')
    pickle.dump(dict, f)

def load_settings(cwd):
    f = open(os.path.join(cwd, meta_data), 'r')
    return pickle.load(f)

def build_command(module, connection, sub_command):
    command = base_command + sub_command
    command = command.replace("[MODULE]", str(module))
    command = command.replace("[CONNECTION]", str(connection))
    command = command.replace("[REPEAT]", str(repeat))
    command += "\r"

    return command

def send_command(command):
    s = None

    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break

    if s is None:
        print "Socket errer:", msg
        sys.exit(1)

    s.sendall(command)
    data = s.recv(1024)
    s.close()

    return repr(data)

usage = """
pytach [nexa/multibrackets/yamaha] [command]
"""

def main():
    args = sys.argv
    if len(args) > 1:
        if args[1] == 'nexa':
            sub_command = nexa.build_command(args[2], args[3])
            command = build_command(1, 1, sub_command)
        elif args[1] == 'multibrackets':
            sub_command = multibrackets.get_command(args[2])
            command = build_command(1, 1, sub_command)
        elif args[1] == 'yamaha':
            sub_command = yamaha.get_command(args[2])
            command = build_command(1, 3, sub_command)
        else:
            print usage
            sys.exit(0)

        print ">", command
        result = send_command(command)
        print "<", result
    else:
        print usage
        sys.exit(0)

if __name__ == '__main__':
    main()