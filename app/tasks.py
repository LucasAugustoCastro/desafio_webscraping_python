from celery import Celery

celery = Celery(__name__)
celery.config_from_object(
  {
    'broker_url': 'pyamqp://guest@rabbitmq//',
    'result_backend': 'redis://redis:6379/0'
  }
)

def send_scraping(cnpj: str):
  task_result = celery.signature("scrape-cnpj", queue='scrape-cnpj', args=(cnpj,)).apply_async()
  return task_result.id