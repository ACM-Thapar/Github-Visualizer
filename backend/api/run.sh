exec gunicorn --certfile=cert.pem --keyfile=key.pem --worker-class gevent --bind 0.0.0.0:6565 app:app
