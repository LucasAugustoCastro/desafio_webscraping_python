import requests as req
from scrap_worker import celery


@celery.task(name='scrape-cnpj')
def scrape_cnpj(cnpj: str):
  print(f'é isso: {cnpj}')