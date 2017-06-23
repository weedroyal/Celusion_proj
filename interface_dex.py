from bottle import route,run,get,post,request,error

query = []

@error(404)
def error404(error):
    return 'No such link exists'






@route('/hello')
def hello():
    return "Hello World!"

@get('/query')
def qry():
    return {'query':query}

@post('/query')
def get_qry():
    question = {'query' : request.json.get('query')}
    query.append(question)
    return {'query':query}

run(host='localhost', port=8080, debug=True)
