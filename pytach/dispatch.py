# -*- coding: utf-8 -*-

import itach
import config
from rest import client
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
            return command
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
        raise NameError("Activity group '%s' does not exist" % group)

def get_connection(device):
    if device in config.config["itach"]["connection"]:
        return {
            u'type': "itach",
            u'port': config.config["itach"]["connection"][device]
        }
    elif device in config.config["rest_client"]:
        connection = {u'type': "rest"}
        connection.update(config.config["rest_client"][device])
        return connection
    else:
        raise NameError("No connection configured for device '%s'" % device)

def device(device_name, command_name):
    connection = get_connection(device_name)
    command = get_command(device_name, command_name)
    if connection["type"] == u"itach":
        command = itach.build_command(1, connection, command["code"])
        send(command)
    elif connection["type"] == u"rest":
        return client.send(command, connection)
    else:
        raise NameError("Unknown type '%s'" % connection["type"])

def activity(activity_group, activity_name):
    activity = get_activity(activity_group, activity_name)
    for command in activity["commands"]:
        device(command["device"], command["command"])

