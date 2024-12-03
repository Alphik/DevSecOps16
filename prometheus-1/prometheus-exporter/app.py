import random
from flask import Flask
from prometheus_client import start_http_server,Gauge,Summary,Counter,Histogram,generate_latest

app = Flask(__name__) 

HTTP_REQUESTS=Counter('HTTP_REQUESTS','count of total http')
AUth_users=Counter('Authenticated_users','count of total http')
HTTP_REQUEST_LATENCY=Histogram('HTTP_LAT','histogram to show the request lat')


@app.before_request
def before_request():
    AUth_users.inc(4)
    HTTP_REQUESTS.inc(1)
    # HTTP_REQUEST_LATENCY.observe(5.4,[])

@app.after_request
def after_request(response):
    return response

@app.get('/metrics')
def metrics():
    return generate_latest(),200

@app.post('/hello') 
def gett_hello():
     
    return 'world !'

@app.get('/math')
def get_math():
    x = random.randrange(1,100)
    y = random.randrange(1,100)
    return f'{x} + {y}  = ?'

app.run(port=8881)