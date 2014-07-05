# -*- coding: utf-8 -*-

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

def device(name, command):
    if name == 'nexa':
        sub_command = nexa.get_command(command)
        command = itach.build_command(1, 1, sub_command, 3)
    elif name == 'multibrackets':
        sub_command = multibrackets.get_command(command)
        command = itach.build_command(1, 1, sub_command)
    elif name == 'yamaha':
        sub_command = yamaha.get_command(command)
        command = itach.build_command(1, 3, sub_command)
    elif name =='epson':
        sub_command = epson.get_command(command)
        command = itach.build_command(1, 2, sub_command)
    else:
        raise NameError("The device '%s' does not exist" % name)

    send(command)

def activity(name, command):
    if name == 'watch':
        if command == 'ps3':
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
        elif command == 'stop':
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
            send(command)
        else:
            raise NameError("The watch cammand '%s' does not exist" % command)
    else:
        raise NameError("The activity '%s' does not exist" % name)