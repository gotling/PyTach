# -*- coding: utf-8 -*-

import os
import re
import bottle
import string
import inspect

from bottle import static_file, template, url, request

import dispatch

static_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/static'
bottle.TEMPLATE_PATH.insert(0, os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) +'/views')

app = application = bottle.Bottle()
bottle.default_app.push(app)
bottle.BaseTemplate.defaults['url'] = url

@app.route('/', name='main')
def main():
    return template('main', devices=dispatch.devices, activities=dispatch.activities, request=request)

@app.route('/static/<filename:path>', name='static')
def static(filename):
    return static_file(filename, root=static_path)

@app.route('/activity/<activity>', name='activity_view', method='GET')
def activity_view(activity):
    return template('activity', activity=dispatch.activities[activity], devices=dispatch.devices, activities=dispatch.activities, request=request)

@app.route('/activity/<activity:path>', name='activity', method='POST')
def activity(activity):
    activity, command = activity.split('/')
    try:
        dispatch.activity(activity, command)
    except NameError, e:
        print "Input error:", e

@app.route('/device/<device>', name='device_view', method='GET')
def device_view(device):
    return template('device', device=dispatch.devices[device], devices=dispatch.devices, activities=dispatch.activities, request=request)

@app.route('/device/<device:path>', name='device', method='POST')
def device(device):
    device, command = device.split('/')
    try:
        result = dispatch.device(device, command)
        return result if result else ""
    except NameError, e:
        print "Input error:", e