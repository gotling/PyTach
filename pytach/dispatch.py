# -*- coding: utf-8 -*-

import itach
import config
import reader

devices = reader.read_path("devices")
activities = reader.read_path("activities")

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
        if command:
            return command["code"]
        else:
            raise NameError("Device '%s' has no command named '%s'" % (device, command_name))
    else:
        raise NameError("Device '%s' deos not exist" % device)

def get_activity(group, activity_name):
    if activities.has_key(group):
        activity = next((item for item in activities[group]["activities"] if item["name"] == activity_name), False)
        if activity:
            return activity
        else:
            raise NameError("Activity group '%s' has no activity named '%s'" (group, activity_name))
    else:
        raise NameError("Activity group '%s' does not exist" % activity)

def get_connection(device):
    if config.connection.has_key(device):
        return config.connection[device]
    else:
        raise NameError("No connection configured for device '%s'" % name)

def device(device_name, command_name):
    connection = get_connection(device_name)
    sub_command = get_command(device_name, command_name)
    command = itach.build_command(1, connection, sub_command) 

    send(command)

def activity(activity_group, activity_name):
    activity = get_activity(activity_group, activity_name)
    for command in activity["commands"]:
        device(command["device"], command["command"])

