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

def device(name, command):
    if name == 'nexa':
        sub_command = nexa.get_command(command)#build_command(arguments['<device>'], arguments['<command>'])
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
    	raise NameError("The device '" + name + "' does not exist")

    log(">", command)
    result = itach.send_command(command)
    log("<", result)