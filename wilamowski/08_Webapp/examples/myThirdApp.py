from bottle import Bottle, route, run, template, get, post, debug, static_file, request, redirect, response

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')

@route('/form')
@route('/form/')
def index(name="Anonymous"):
    return template('formExample', name=name)

@route('/formProcess')
@route('/formProcess/')
@route('/formProcess', method='POST')
@route('/formProcess/', method='POST')
def index(name="Anonymous"):
    print(request.forms.keys())
    myDict= {k:request.forms.getunicode(k) for k in request.forms.keys()}
    return template('formExampleProc', name=name, myDict=myDict)

@route('/charts/')
@route('/charts')
def index(name="Anonymous"):
    
    
#         labels: ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sut', 'Sun'],
#     datasets: [{
#       label: 'apples',
#       data: [12, 19, 3, 17, 6, 3, 7],
#       backgroundColor: "rgba(153,255,51,0.4)"
#     }, {
#       label: 'oranges',
#       data: [2, 29, 5, 5, 2, 3, 10],
#       backgroundColor: "rgba(255,153,0,0.4)"
#     }]
#   }
    chartData = {
"labels":['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sut', 'Sun'],
    "data" : {
        "apples":[12, 19, 3, 17, 6, 3, 7],
        "oranges":[2, 29, 5, 5, 2, 3, 10],
        "pears":[22, 39, 15, 16, 22, 31, 14],
    }
}
    return template('charts', name=name, chartData=chartData)

@route('/')
def index(name="Maciej"):
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}
    return template('index', message=messDict.get("ok", ""), loginName=name, text="loremipsum example text")


@route('/bestMovies')
def index(name="Maciej"):
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}
    movies = [{"title":"Star Wars",
     "score":10,
     "review":"Lorem ipsum"},
    {"title":"Django",
     "score":9.9,
     "review":"Lorem ipsum"},
    {"title":"Fight Club",
     "score":9.95,
     "review":"Lorem ipsum"}]
     

    return template('movies', message=messDict.get("ok", ""), loginName=name, movies=movies)

run(host='localhost', port=8081, debug=True, reloader=True)