# -*- coding: utf-8 -*-

import re
import sys
import socket
import struct

from config import config

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

    for res in socket.getaddrinfo(config["itach"]["host"], config["itach"]["port"], socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
            s.settimeout(config["itach"]["timeout"])
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

def discover():
    p = re.compile((r'AMXB<-UUID=GlobalCache_(?P<UUID>.{12}).+'
        r'Model=iTach(?P<Model>.+?)>.+'
        r'Revision=(?P<Revision>.+?)>.+'
        r'Config-URL=http://(?P<IP>.+?)>.+'
        r'PCB_PN=(?P<PN>.+?)>.+'
        r'Status=(?P<Status>.+?)>'))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(30)
    s.bind(('', 9131))

    group = socket.inet_aton('239.255.250.250')
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        try:
            data = s.recv(1024)
            match = p.match(data)
            if match:
                print "iTach found!"
                print "IP:\t\t%s" % match.group('IP')
                print "UUID:\t\t%s" % match.group('UUID')
                print "Model:\t\t%s" % match.group('Model')
                print "Revision:\t%s" % match.group('Revision')
                print "Part number:\t%s" % match.group('PN')
                print "Status:\t\t%s" % match.group('Status')

                return
        except socket.timeout:
            print "Could not find an iTach on the network"
        finally:
            s.close()
            return
