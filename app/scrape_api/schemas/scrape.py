from pydantic import BaseModel

class RequestScrape(BaseModel):
  cnpj: str

class ScrapeResponse(BaseModel):
  task_id: str
