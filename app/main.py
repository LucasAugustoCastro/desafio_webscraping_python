from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/result/{task_id}")
def read_root(task_id) -> Union[str, int]:
    return f"Hello, world! {task_id}"

@app.post("/scrape")
def scrape() -> Union[str, int]:
    return "Scraping..."