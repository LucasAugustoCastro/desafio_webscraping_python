from typing import Union, Optional
from pydantic import BaseModel
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

class ResultResponse(BaseModel):
  task_id: str
  task_status: str
  result: Union[ResultSuccessScrape, ResultErrorScrape, None]