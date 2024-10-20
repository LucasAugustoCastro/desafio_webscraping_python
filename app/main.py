from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import tasks

app = FastAPI()

class ResultSuccessScrape(BaseModel):
  cnpj: str
  inscricao_estadual: str
  cadastro_atualizado_em: str
  nome_empresarial: str
  contribuinte: str
  nome_fantasia: Optional[str]
  endereco: str
  atividade_principal: str
  regime_de_apuracao: str
  situacao_cadastral_vigente: str
  data_de_cadastramento: str
  data_de_consulta: str

class ResultErrorScrape(BaseModel):
  error: str

class ResponseResult(BaseModel):
  task_id: str
  task_status: str
  result: Union[ResultSuccessScrape, ResultErrorScrape, None]


@app.get("/result/{task_id}", response_model=ResponseResult)
def get_tasks_status(task_id):
  tasks_result = tasks.celery.AsyncResult(task_id)
  status = tasks_result.status
  result = tasks_result.result if tasks_result.successful() else None
  return {
    "task_id": task_id,
    "task_status": status,
    "result": result
  }

class Item(BaseModel):
  cnpj: str

class TaskResponse(BaseModel):
  task_id: str

@app.post("/scrape", response_model=TaskResponse)
def scrape(item:Item):
  task_id = tasks.send_scraping(item.cnpj)
  return {"task_id": str(task_id)}
    