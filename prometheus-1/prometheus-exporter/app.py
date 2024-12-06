import random
import time
from flask import Flask
from prometheus_client import start_http_server,Gauge,Summary,Counter,Histogram,generate_latest

app = Flask(__name__) 

HTTP_REQUESTS=Counter('http_request_total','count of total http',['endpoint','method','code'])
AUTH_USER=Counter('Authenticated_users_requests_total','count of total http')
HTTP_REQUEST_LATENCY=Histogram('http_request_duration_seconds','histogram to show the request lat',['endpoint','method'])


@app.get('/metrics')
def metrics():
    start_time= time.time()
    HTTP_REQUESTS.labels(endpoint='/metrics',method='get',code=200).inc(1)
    duration=time.time() - start_time
    HTTP_REQUEST_LATENCY.labels(endpoint='/metrics',method='get').observe(duration)
    return generate_latest()
@app.get('/login')
def login():
    if random.randint(0,100) > 50:
        HTTP_REQUESTS.labels(endpoint='/login',method='get',code='200').inc(1)
        return '200'
    else:
        HTTP_REQUESTS.labels(endpoint='/login',method='get',code='400').inc(1)
        return '400'

app.run(port=5001)