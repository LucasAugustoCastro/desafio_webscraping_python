from celery_app import celery

def send_scraping(cnpj: str):
  task_result = celery.signature("scrape-cnpj", queue='scrape-cnpj', args=(cnpj,)).apply_async()
  return task_result.id