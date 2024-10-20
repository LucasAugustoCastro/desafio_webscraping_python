from scrape_api.celery_app import celery

def send_scraping(cnpj: str):
  task_result = celery.signature("scrape-cnpj", queue='scrape-cnpj', args=(cnpj,)).apply_async()
  return task_result.id

def get_task_status(task_id: str):
  tasks_result = celery.AsyncResult(task_id)
  status = tasks_result.status
  result = tasks_result.result if tasks_result.successful() else None
  return {
    "task_id": task_id,
    "task_status": status,
    "result": result
  }