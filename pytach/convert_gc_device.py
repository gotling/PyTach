#!/usr/bin/env python

import argparse
import struct
import csv
import json
import os
import sys

def convert_gc (filename, name, description):

	debug = False
	commands = []

	root, ext = os.path.splitext(filename)
	root, basename = os.path.split(root)

        if name == None:
		name = basename

        if description == None:
		description = basename

	with open(filename, 'rb') as csvfile:                                                                                                                                   
		sr = csv.reader(csvfile, delimiter=',')
		for row in sr:
			if row != []:
				if row[0] != 'function':
	 				if debug:
						print row[0]
						print row[1]
	                                command, row[1] = row[1].partition(',')[::2]
	                                address, row[1] = row[1].partition(',')[::2]
	                                ID, row[1] = row[1].partition(',')[::2]
	                                frequency, row[1] = row[1].partition(',')[::2]
	                                repeat, row[1] = row[1].partition(',')[::2]
					a = dict(name=row[0].replace(' ','_'), description=row[0].lower(), code=row[1].rstrip())
	                                if debug:
						print a['name']
						print a['code']
					commands.append(a)
			
	file = dict(name=name, description=description, commands=commands)
	if debug:
		print commands
		print file

	with open(basename+'.json', 'w') as outfile:
    		json.dump(file, outfile,indent=1)
			
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts files from the Global Cache Database (https://irdb.globalcache.com/) to device.json files')

    parser.add_argument('-n', '--name',        nargs=1, dest='name',        help='name of device',            action='store', default = [ None ])
    parser.add_argument('-d', '--description', nargs=1, dest='description', help='description of the device', action='store', default = [ None ])
    parser.add_argument('file', action='append', nargs=1, help='file to be converted', default=argparse.SUPPRESS)

 
    args = parser.parse_args() 
    if 'file' not in args:
	parser.print_usage()
	sys.exit(1)

    convert_gc(args.file[0][0], args.name[0], args.description[0])
 
