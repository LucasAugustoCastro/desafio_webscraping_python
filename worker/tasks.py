from worker import celery


@celery.task(name='scrape-cnpj')
def scrape_cnpj(cnpj: str):
  pass