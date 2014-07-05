import bottle
from bottle import route, run
from web import web
import config

app = application = bottle.Bottle()
app.merge(web.app)

config.arguments['--verbose'] = True

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8082, debug=True)
