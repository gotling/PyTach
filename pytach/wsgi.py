import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import bottle

import config
from web import web

app = application = bottle.Bottle()
app.merge(web.app)

config.arguments['--verbose'] = True

mount_path = os.getenv("APP_MOUNT_PATH", "/")
app.config['APP_MOUNT_PATH'] = mount_path

app.mount(mount_path,  app)
bottle.BaseTemplate.defaults['APP_MOUNT_PATH'] = mount_path
