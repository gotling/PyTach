# -*- coding: utf-8 -*-

import itach
import config
import reader

devices = reader.read_path("devices")

def log(prompt, command):
    if config.arguments['--verbose']:
        print prompt, command

def send(command):
    log(">", command)
    result = itach.send_command(command)
    log("<", result)

def get_command(device, command_name):
    if devices.has_key(device):
        command = next((item for item in devices[device]["commands"] if item["name"] == command_name), False)
        if command == False:
            raise NameError("Device '%s' has no command named '%s'" % (device, command_name))
        else:
            return command["code"]
    else:
        raise NameError("Device '%s' deos not exist" % device)

def get_connection(device):
    if config.connection.has_key(device):
        return config.connection[device]
    else:
        raise NameError("No connection configured for device '%s'" % name)

def device(name, command_name):
    connection = get_connection(name)
    sub_command = get_command(name, command_name)
    command = itach.build_command(1, connection, sub_command) 

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