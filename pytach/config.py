# -*- coding: utf-8 -*-
import os
import pickle

itach_host = "192.168.0.22"
itach_port = 4998
timeout = 2

meta_data = '.pytach_settings'
arguments = {}
connection = {
	'nexa': 1,
	'multibrackets': 1,
	'yamaha': 3,
	'epson': 2
}

def save_settings(cwd, dict):
    f = open(os.path.join(cwd, meta_data), 'w')
    pickle.dump(dict, f)

def load_settings(cwd):
    f = open(os.path.join(cwd, meta_data), 'r')
    return pickle.load(f)