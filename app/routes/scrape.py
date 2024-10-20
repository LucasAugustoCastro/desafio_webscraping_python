from fastapi import APIRouter

import tasks
from schemas import RequestScrape, ScrapeResponse, ResultResponse

router = APIRouter()

@router.get("/result/{task_id}", response_model=ResultResponse)
def get_tasks_status(task_id):
  tasks_result = tasks.celery.AsyncResult(task_id)
  status = tasks_result.status
  result = tasks_result.result if tasks_result.successful() else None
  return {
    "task_id": task_id,
    "task_status": status,
    "result": result
  }

@router.post("/scrape", response_model=ScrapeResponse)
def scrape(request:RequestScrape):
  task_id = tasks.send_scraping(request.cnpj)
  return {"task_id": str(task_id)}
    