# -*- coding: utf-8 -*-

baseCommand = "1,13,39,13,39,13,39,13,39,13,39,13,39,13,39,13,39,13,39,[DEVICE],13,39,13,39,13,39,13,39,13,39,13,39,13,39,39,13,13,39,39,13,13,39,[STATE],13,427";

def build_command(device, off):
	command = baseCommand.replace("[DEVICE]", get_device(device))
	command = command.replace("[STATE]", get_state(off))

	return command

def get_device(device):
	return {
		1: "13,39,13,39,13,39",
		2: "39,13,13,39,13,39",
		3: "13,39,13,39,39,13",
	}.get(int(device), "")

def get_state(off):
	if off in ('off', 'OFF', 0, True):
		return "13,39";
	else:
		return "39,13";