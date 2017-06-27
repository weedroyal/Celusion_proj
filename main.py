from bottle import route,run,get,post,request,error
from question import processing

query = ''

@route('/')
def index():
    greet = "Hello! I'm Dexter\n"
    greet1 = "How may I help you?"
    return greet , greet1

@route('/hello')
def test():
    return 'Server is running'

@post('/query')
def pst_qry():
    global query
    question = request.json.get('query')
    query = str(question.lower())
    result = processing(query)
    return {'query' : query, 'result': result}


@get('/query')
def gt_qry():
    return {'query': query}



run(host = 'localhost',port = 8080,debug = True,server='tornado')
