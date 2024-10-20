import pytest
from scrap_worker.scrape_sintegra import ScrapeSintegra

@pytest.fixture
def scraper(driver):
    return ScrapeSintegra(driver)

def test_scrape(mocker, scraper):
    mocker.patch.object(scraper.driver, 'get')
    mocker.patch.object(scraper.driver, 'find_element')
    mocker.patch('scrap_worker.scrape_sintegra.WebDriverWait')

    scraper.scrape('00012377000160')

    scraper.driver.get.assert_called_once_with('http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html')
    scraper.driver.find_element.assert_called()

def test_extract_page(scraper):
    page = None
    with open('worker/tests/mock_data/cnpj_page.html') as f:
        page = f.read()
    data = scraper.extract_page(page)
    assert data["cnpj"] == "00.006.486/0001-75"
    assert data["inscricao_estadual"] == "10.114.063-0"
    assert data["cadastro_atualizado_em"] == "13/02/2015 11:03:28"
    assert data["nome_empresarial"] == "L. M. CARVALHO & CIA LTDA EPP"
    assert data["contribuinte"] == "Sim"
    assert data["nome_fantasia"] == "DROGARIA SAO FRANCISCO DE ASSIS"
    assert data["endereco"] == "PRACA  PIRINEUS DA SILVEIRA, nº 128, S CENRAL  - ANICUNS GO, CEP: 76.170-000"
    assert data["atividade_principal"] == "4771701 - Comércio varejista de produtos farmacêuticos, sem manipulação de fórmulas"
    assert data["regime_de_apuracao"] == "Micro EPP/Simples Nacional"
    assert data["situacao_cadastral_vigente"] == "Ativo - HABILITADO"
    assert data["data_de_cadastramento"] == "08/08/1990"
    assert data["data_de_consulta"] == "20/10/2024 18:37:04"

    