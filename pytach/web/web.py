# -*- coding: utf-8 -*-

import os
import re
import bottle
import string
import inspect

from bottle import static_file

import config
import dispatch

static_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/static'

app = application = bottle.Bottle()

@app.route('/')
def main():
    return static_file('main.html', root=static_path)

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=static_path)

@app.route('/activity/<activity:path>', method='POST')
def activity(activity):
    activity, command = activity.split('/')
    try:
        dispatch.activity(activity, command)
    except NameError, e:
        print "Input error:", e

@app.route('/device/<device:path>', method='POST')
def device(device):
    device, command = device.split('/')
    try:
        dispatch.device(device, command)
    except NameError, e:
        print "Input error:", e