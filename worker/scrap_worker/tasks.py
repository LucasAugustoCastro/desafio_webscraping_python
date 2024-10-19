from scrap_worker import celery
from scrap_worker.scrape_sintegra import ScrapeSintegra

@celery.task(name='scrape-cnpj')
def scrape_cnpj(cnpj: str):
  try:
    scrapper = ScrapeSintegra()
    page = scrapper.scrape(cnpj)
    data = scrapper.extract_page(page)
  except Exception as e:
    data = {'error': str(e)}
  return data
  