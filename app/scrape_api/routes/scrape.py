from fastapi import APIRouter

from scrape_api import tasks
from scrape_api.schemas import RequestScrape, ScrapeResponse, ResultResponse

router = APIRouter()

@router.get("/result/{task_id}", response_model=ResultResponse)
def get_tasks_status(task_id):
  task_data = tasks.get_task_status(task_id)
  return task_data

@router.post("/scrape", response_model=ScrapeResponse)
def scrape(request:RequestScrape):
  task_id = tasks.send_scraping(request.cnpj)
  return {"task_id": str(task_id)}
    