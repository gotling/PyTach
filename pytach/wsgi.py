import bottle

import config
from web import web

app = application = bottle.Bottle()
app.merge(web.app)

config.arguments['--verbose'] = True
