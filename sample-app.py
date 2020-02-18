import os
import time

from flask import Flask, render_template_string, abort
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram

app = Flask(__name__)

# A counter to count the total number of HTTP requests.
REQUEST_COUNT = Counter('http_requests_total', 'Total Number HTTP Requests', ['method', 'endpoint', 'status_code'])

# A gauge to monitor the total number of requests in-progress.
IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')

# A histogram to measure the HTTP requests' latency.
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency in seconds')

# Standard Flask route stuff.
@app.route('/')
# Helper annotation to measure how long a method takes and save as a histogram metric.
@REQUEST_LATENCY.time()
# Helper annotation to increment a gauge when entering the method and decrementing when leaving.
@IN_PROGRESS.track_inprogress()

def hello():
    VER = os.environ.get('VERSION')
    HOST = os.uname()[1]
    REQUEST_COUNT.labels(method='GET', endpoint="/", status_code=200).inc()  # Incrementing the counter
    if VER and HOST is not None:
        return "Hello World! Running on Host: " + HOST + " Version: " + VER + "\n"
    else:
        return "Hello World!"

@app.route('/metrics')
@IN_PROGRESS.track_inprogress()
@REQUEST_LATENCY.time()
def metrics():
    REQUEST_COUNT.labels(method='GET', endpoint="/metrics", status_code=200).inc()
    return generate_latest(REGISTRY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
