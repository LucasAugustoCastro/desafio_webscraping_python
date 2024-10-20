import os 

from kombu import Queue

RESULT_BACKEND = os.environ['RESULT_BACKEND']
BROKER_URL = os.environ['BROKER_URL']

class CeleryConfig(object):
  broker_url = BROKER_URL
  result_backend = RESULT_BACKEND
  task_queues = {
    Queue(name="scrape-cnpj"),
  }
  task_routes = {
    'scrape-cnpj': {'queue': 'scrape-cnpj'},
  }
