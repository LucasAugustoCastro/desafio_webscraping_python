from celery import Celery
from kombu import Queue

class Config(object):
  broker_url = 'amqp://guest:guest@localhost:5672/'
  result_backend = 'redis://localhost:6379/0'
  task_queues = {
    Queue(name="scrape-cnpj"),
  }
  task_routes = {
    'scrape-cnpj': {'queue': 'scrape-cnpj'},
  }

celery = Celery(__name__)
celery.config_from_object(Config)