from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    if '' not in [a, b]:
        a, b = int(a), int(b)
        x = str(a + b)
        y = str(a * b)

    if '' in [a, b]:
        x = str(0)
        y = str(0)

    response_body = html%{
        'sum': x,
        'prod': y,
        }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
