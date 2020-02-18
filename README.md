# Sample Flask Prometheus Application

This is a sample application written in Python Flask with the Python Prometheus client.

- Python 3.7
- Flask==1.1.1
- prometheus-client==0.7.1

## Build the container

```console
$ docker build -t sample-flask-prometheus-app .
```

## Run the container

To access the application on your Docker host, you will need to publish the port by specifying the `-p` option, for example `-p 8080:5000`.

```console
$ docker run -d --name=my-flask-app -p 8080:5000 -e VERSION=0.1  nirmalpathak/sample-flask-prometheus-app
```

If you do not specify environment variable `VERSION` using `-e` option then application will only return `Hello World!`
