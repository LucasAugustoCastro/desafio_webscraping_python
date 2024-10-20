from typing import Union, Optional
from pydantic import BaseModel
class ResultSuccessScrape(BaseModel):
  cnpj: Optional[str]
  inscricao_estadual: Optional[str]
  cadastro_atualizado_em: Optional[str]
  nome_empresarial: Optional[str]
  contribuinte: Optional[str]
  nome_fantasia: Optional[str]
  endereco: Optional[str]
  atividade_principal: Optional[str]
  regime_de_apuracao: Optional[str]
  situacao_cadastral_vigente: Optional[str]
  data_de_cadastramento: Optional[str]
  data_de_consulta: Optional[str]

class ResultErrorScrape(BaseModel):
  error: str

class ResultResponse(BaseModel):
  task_id: str
  task_status: str
  result: Union[ResultSuccessScrape, ResultErrorScrape, None]