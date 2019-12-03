from bottle import Bottle, route, run, template, get, post, debug, static_file, request, redirect, response

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')

@route('/hello/<name>')
@route('/hello/')
@route('/hello')
def index(name="Anonymous"):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/bye/<name>')
@route('/bye/')
@route('/bye')
def index(name="Anonymous"):
    return template('<b>Bye {{name}}</b>!', name=name)

@route('/')
def index(name="Maciej"):
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}
    return template('index', message=messDict.get("none", ""), loginName=name)

	
	
run(host='localhost', port=8080, debug=True, reloader=True)