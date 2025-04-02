# gunicorn.conf.py
loglevel = "debug"
bind = "127.0.0.1:8000"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
wsgi_app= "app.main:app" 