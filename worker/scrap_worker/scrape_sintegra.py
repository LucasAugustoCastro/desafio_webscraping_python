import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

class ScrapeSintegra:
  def __init__(self, driver=None):
    if not driver:
      firefox_options = Options()
      firefox_options.add_argument('--headless')
      service = Service('/usr/local/bin/geckodriver')
      self.driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
      self.driver = driver

  def scrape(self, cnpj):
    try:
      self.driver.get('http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html')
      radio_cnpj = self.driver.find_element(By.ID,'rTipoDocCNPJ')
      radio_cnpj.click()
      input_cnpj = self.driver.find_element(By.ID,'tCNPJ')
      input_cnpj.send_keys(cnpj)
      button_consultar = self.driver.find_element(By.NAME,'btCGC')
      button_consultar.click()
      WebDriverWait(self.driver, 10).until(
          EC.visibility_of_element_located((By.CLASS_NAME, "container"))
      )
      data = self.driver.page_source
    except Exception as e:
      raise e
    finally:
      self.driver.quit()
    return data
  
  def extract_page(self, data):
    soup = BeautifulSoup(data, 'html.parser')
    data = {
      'cnpj': self._get_field(soup, 'CNPJ'),
      'inscricao_estadual': self._get_field(soup, 'Inscrição Estadual'),
      'cadastro_atualizado_em': self._get_field(soup, 'Cadastro Atualizado em'),
      'nome_empresarial': self._get_field(soup, 'Nome Empresarial'),
      'contribuinte':self._get_field(soup, 'Contribuinte?'),
      'endereco': self._get_field(soup, 'Endereço Estabelecimento', tag='div'),
      'atividade_principal': self._get_field(soup, 'Atividade Principal'),
      'regime_de_apuracao': self._get_field(soup, 'Regime de Apuração'),
      'situacao_cadastral_vigente': self._get_field(soup, 'Situação Cadastral Vigente'),
      'data_de_cadastramento': self._get_field(soup, 'Data de Cadastramento'),
      'data_de_consulta': self._get_field(soup, 'Data da Consulta'),
      'nome_fantasia': self._get_field(soup, 'Nome Fantasia')
    }
    return data
  
  def _get_field(self, soup, field, tag='span'):
    field = soup.find(tag, text=re.compile(field))
    if not field:
      return None
    return field.find_next('span', class_='label_text').get_text(strip=True)