# -*- coding: utf-8 -*-
import os
import pickle

meta_data='.pytach_settings'
arguments={}

def save_settings(cwd, dict):
    f = open(os.path.join(cwd, meta_data), 'w')
    pickle.dump(dict, f)

def load_settings(cwd):
    f = open(os.path.join(cwd, meta_data), 'r')
    return pickle.load(f)