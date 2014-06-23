# -*- coding: utf-8 -*-

import sys
import socket

HOST = "192.168.0.22"
PORT = 4998
timeout = 2
module = 1
connection = 1
base_command = "sendir,[MODULE]:[CONNECTION],1,38000,[REPEAT],";

def build_command(module, connection, sub_command, repeat=3):
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
            s.settimeout(timeout)
        except socket.error as msg:
            s = None
            continue
        
        try:
            s.connect(sa)
        except (socket.error, socket.timeout) as msg:
            s.close()
            s = None
            continue
        break

    if s is None:
        print "Socket errer:", msg
        return

    s.sendall(command)
    data = s.recv(1024)
    s.close()

    return repr(data)