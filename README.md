PyTach
================
Python library for communicating with GlobalCache iTach IR/RF device.

Features
================
* Command line interface
* REST interface
* Web interface
* Arduino I/O

Command line usage
================
### Control device
	pytach.py device <device> <command>

List available devices with *pytach.py --help*

### Activity
	pytach.py activity <activity> <command>

List available activities with *pytach.py --help*

### Start web server
	pytach.py --web

Accessible on [localhost:8099](http://localhost:8099)

### Start Arduino listener
	pytach.py --arduino

Installation
================
Home Assistant
----------------
Clone repoistory to you *addons* folder.
In Home Assistant, open Add-ons and install.

Web UI will be available on `host:8000`.

Make devices and commands available by editing *configuration.yaml* listing commands like this:

```
rest_command:
  nexa_1_on:
    url: "http://localhost:8000/device/nexa/1:on"
    method: post
  nexa_1_off:
    url: "http://localhost:8000/device/nexa/1:off"
    method: post
```

Debian
----------------

	cd /opt
	sudo su - 
	git clone https://github.com/gotling/PyTach.git
	cd PyTach
	pip install -r requirements.txt

Standalone development server
----------------
Make PyTach available at *http://server:8099*

	ln -s /opt/PyTach/scripts/pytach-init.sh /etc/init.d/pytach
	chmod +x /etc/init.d/pytach
	update-rc.d pytach defaults
	service pytach start

nginx + uWSGI (recommended)
----------------
Make PyTach available at *http://server/pytach*

	apt-get install uwsgi uwsgi-plugin-python nginx
	ln -s /opt/PyTach/scripts/pytach-uwsgi.ini /etc/uwsgi/apps-enabled/
	service uwsgi restart

Add content of *scripts/nginx-config* to */etc/nginx/sites-available/default*

	service nginx restart

Arduino listener
----------------
Make Arduino listener start on boot.

	ln -s /opt/PyTach/scripts/pytach-arduino-init.sh /etc/init.d/pytach-arduino
	chmod +x /etc/init.d/pytach-arduino
	update-rc.d pytach-arduino defaults
	service pytach-arduino start

Acknowledgements
================
Bottle
----------------
Copyright © 2012 Marcel Hellkamp

http://bottlepy.org/

License: MIT License

docopt
----------------
Copyright © 2012 Vladimir Keleshev

http://docopt.org/

License: MIT License

microajax
----------------
Copyright © 2008 Stefan Lange-Hegermann

https://code.google.com/p/microajax/

License: BSD License

Pure
----------------
Copyright © 2014 Yahoo! Inc

http://purecss.io/

License: BSD License

pySerial
----------------
Copyright © 2001-2013 Chris Liechti

http://pyserial.sourceforge.net/

License: Python Software Foundation License

pytach
----------------
Copyright © 2012 Mark McWilliams

https://github.com/moolicious/pytach

License: MIT License