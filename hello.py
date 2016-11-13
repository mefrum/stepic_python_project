def app(environ, start_response):
    '''Fucntino parse http req and return attribute'''
    start_response("200 OK", [("Content-Type", "text/plain")])
    body = environ['QUERY_STRING'].split('&')
    i = 0
    while i < len(body):
        body[i] = body[i] + '\n'
        i += 1
    bodybites = [body[i].encode() for i in range(len(body))]
    return bodybites    