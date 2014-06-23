# -*- coding: utf-8 -*-

import string
from bottle import route, run, static_file

import itach
import config
import devices.nexa as nexa
import devices.yamaha_rx350 as yamaha
import devices.epson_eh_tw3200 as epson
import devices.multibrackets as multibrackets

def log(prompt, command):
    if config.arguments['--verbose']:
        print prompt, command

def send(command):
    log(">", command)
    result = itach.send_command(command)
    log("<", result)

@route('/')
def hello():
    return static_file('main.html', root='/opt/PyTach/pytach/web/static')

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='/opt/PyTach/pytach/web/static')

@route('/activity/<activity:path>', method='POST')
def activity(activity):
    activity = activity.split('/')
    if activity[0] == 'watch_ps3':
        sub_command = epson.get_command('power')
        command = itach.build_command(1, 2, sub_command)
        send(command)

        sub_command = nexa.build_command(1, "off")
        command = itach.build_command(1, 1, sub_command)
        send(command)

        sub_command = multibrackets.get_command('down')
        command = itach.build_command(1, 1, sub_command)
        send(command)

        sub_command = yamaha.get_command('dtv')
        command = itach.build_command(1, 3, sub_command)
        send(command)
    elif activity[0] == 'watch_ended':
        sub_command = epson.get_command('power')
        command = itach.build_command(1, 2, sub_command)
        send(command)

        sub_command = epson.get_command('power')
        command = itach.build_command(1, 2, sub_command)
        send(command)

        sub_command = nexa.build_command(1, "on")
        command = itach.build_command(1, 1, sub_command)
        send(command)

        sub_command = multibrackets.get_command('up')
        command = itach.build_command(1, 1, sub_command)
        send(command)

        sub_command = yamaha.get_command('cd')
        command = itach.build_command(1, 3, sub_command)

@route('/device/<device:path>', method='POST')
def device(device):
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

run(host='0.0.0.0', port=8082, debug=True)
