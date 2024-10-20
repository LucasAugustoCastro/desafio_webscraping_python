import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

class ScrapeSintegra:
  def __init__(self):
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    service = Service('/usr/local/bin/geckodriver')
    self.driver = webdriver.Firefox(service=service, options=firefox_options)

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
      'cnpj':soup.find('span', class_='label_title', text=re.compile('CNPJ')).find_next('span', class_='label_text').get_text(strip=True),
      'inscricao_estadual':soup.find('span', class_='label_title', text=re.compile('Inscrição Estadual')).find_next('span', class_='label_text').get_text(strip=True),
      'cadastro_atualizado_em':soup.find('span', class_='label_title', text=re.compile('Cadastro Atualizado em')).find_next('span', class_='label_text').get_text(strip=True),
      'nome_empresarial':soup.find('span', class_='label_title', text=re.compile('Nome Empresarial')).find_next('span', class_='label_text').get_text(strip=True),
      'contribuinte':soup.find('span', class_='label_title', text=re.compile('Contribuinte?')).find_next('span', class_='label_text').get_text(strip=True),
      'endereco':soup.find('div', class_='label_title', text=re.compile('Endereço Estabelecimento')).find_next('span', class_='label_text').get_text(strip=True),
      'atividade_principal':soup.find('span', class_='label_text', text=re.compile('Atividade Principal')).find_next('span', class_='label_text').get_text(strip=True),
      'regime_de_apuracao':soup.find('span', class_='label_title', text=re.compile('Regime de Apuração')).find_next('span', class_='label_text').get_text(strip=True),
      'situacao_cadastral_vigente':soup.find('span', class_='label_title', text=re.compile('Situação Cadastral Vigente')).find_next('span', class_='label_text').get_text(strip=True),
      'data_de_cadastramento':soup.find('span', class_='label_title', text=re.compile('Data de Cadastramento')).find_next('span', class_='label_text').get_text(strip=True),
      'data_de_consulta':soup.find('span', class_='label_title', text=re.compile('Data da Consulta')).find_next('span', class_='label_text').get_text(strip=True),
      'nome_fantasia': None,
    }
    trade_name = soup.find('span', class_='label_title', text=re.compile('Nome Fantasia'))
    if trade_name:
      trade_name = trade_name.find_next('span', class_='label_text').get_text(strip=True)
      data['nome_fantasia'] = trade_name
    
    return data