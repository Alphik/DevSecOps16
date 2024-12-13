# Prometheus

## Introduction

Prometheus is an open-source monitoring and alerting system that excels at collecting time-series metrics. It's particularly well-suited for cloud-native environments and microservices architectures. In this tutorial, we'll delve into the fundamentals of Prometheus, PromQL, Prometheus Client for Python, and its integration with Grafana.

## Installation

### Install Prometheus Server

Docker:

```Bash
docker run -d -p 9090:9090 --name prometheus prometheus/prometheus
```

Manual: Refer to the official documentation for detailed instructions.

### Install Grafana

Docker:

```Bash
docker run -d -p 3000:3000 --name grafana grafana/grafana
```

Manual: Follow the official installation guide.

## Configuring Prometheus

Create a Prometheus Configuration File (prometheus.yml):

```YAML
global:
  scrape_interval: 15s # How often to scrape targets

scrape_configs:
  - job_name: 'example-app'
    static_configs:
      - targets: ['localhost:8000']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
```

### Start the Prometheus Server:

Docker: Start the Prometheus Docker Container
Use the -v option to mount your local prometheus.yml file into the container.

```bash
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

Manual: Start the Prometheus server using the configuration file.

```bash
./prometheus --config.file=prometheus.yml
```

### Using Prometheus Client for Python

## Install the Library:

```Bash
pip install prometheus_client
```

### Create Metrics:

```Python
from prometheus_client import Counter, Gauge, Histogram

# Counter metric
requests_total = Counter('requests_total', 'Total number of requests')

# Gauge metric
temperature = Gauge('temperature_celsius', 'Temperature in Celsius')

# Histogram metric
request_latency = Histogram('request_latency_seconds', 'Request latency distribution')
```

Increment Counters and Set Gauge Values:

```Python
requests_total.inc()
temperature.set(25.0)
request_latency.observe(0.5)
```

Start the HTTP Server:

```Python
from prometheus_client import start_http_server

start_http_server(8000)
```

## Querying Prometheus with PromQL

PromQL (Prometheus Query Language) is a powerful query language for time-series data. Here are some basic examples:

- Instant Vector:
- Code snippet
- http_requests_total
- Use code with caution.

Range Vector:

```promql
http_requests_total[5m]
```

Rate:
rate(http_requests_total[5m])

Increase:
increase(http_requests_total[5m])

## another example

```python
from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import start_http_server

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('request_count', 'Total webapp requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds', ['endpoint'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    with REQUEST_LATENCY.labels(endpoint='/').time():
        return "Hello, Prometheus!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus scrapes this port
    app.run(host='0.0.0.0', port=8000)
```
