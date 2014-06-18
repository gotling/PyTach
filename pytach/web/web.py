# -*- coding: utf-8 -*-

import string
from bottle import route, run, static_file

import itach
from devices import nexa as nexa
from devices import multibrackets as multibrackets
from devices import yamaha_rx350 as yamaha
import devices.epson_eh_tw3200 as epson

def send(command):
    print ">", command
    result = itach.send_command(command)
    print "<", result

@route('/')
def hello():
    return static_file('main.html', root='web/static')

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='web/static')

@route('/device/<device:path>', method='POST')
def device(device):
    print device
    device = device.split('/')
    if device[0] == 'nexa':
        if len(device) == 3:
            sub_command = nexa.build_command(device[1], device[2])
            command = itach.build_command(1, 1, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    elif device[0] == 'multibrackets':
        if len(device) == 2:
            sub_command = multibrackets.get_command(device[1])
            command = itach.build_command(1, 1, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    elif device[0] == 'yamaha':
        if len(device) == 2:
            sub_command = yamaha.get_command(device[1])
            command = itach.build_command(1, 3, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    elif device[0] == 'epson':
        if len(device) == 2:
            sub_command = epson.get_command(device[1])
            command = itach.build_command(1, 2, sub_command)
            send(command)
        else:
            print 'Incorrect parameters'
    else:
        print 'Unknown device'

run(host='192.168.0.26', port=8080, debug=True)