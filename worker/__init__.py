from celery import Celery
from kombu import Queue

class Config(object):
  broker_url = 'pyamqp://guest@localhost//'
  result_backend = 'redis://localhost:6379/0'
  task_queues = {
    Queue(name="scrape-cnpj"),
  }
  task_routes = {
    'scrape-cnpj': {'queue': 'scrape-cnpj'},
  }

celery = Celery(__name__)
celery.config_from_object(Config)