from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/result/{task_id}")
def read_root(task_id) -> Union[str, int]:
  return f"Hello, world! {task_id}"


class Item(BaseModel):
  cnpj: str

@app.post("/scrape")
def scrape(item:Item) -> Union[str, int]:
  from tasks import send_scraping
  task_id = send_scraping(item.cnpj)
  return task_id
    