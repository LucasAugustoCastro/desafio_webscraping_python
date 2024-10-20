import pytest
from scrape_api.schemas.scrape import RequestScrape

def test_scrape_route(client, mocker):
    mocker.patch('scrape_api.tasks.send_scraping', return_value="mock_task_id")
    response = client.post("/scrape", json={"cnpj": "00012377000160"})
    assert response.status_code == 200
    assert response.json() == {"task_id": "mock_task_id"}

def test_get_tasks_status(client, mocker):
    mocker.patch('scrape_api.tasks.get_task_status', return_value={
        "task_status": "completed",
        "task_id": "mock_task_id",
        "result": {
            "cnpj": "00012377000160",
            "inscricao_estadual": "123456789",
            "cadastro_atualizado_em": "2023-10-01",
            "nome_empresarial": "Empresa Exemplo Ltda",
            "contribuinte": "Sim",
            "nome_fantasia": "Exemplo",
            "endereco": "Rua Exemplo, 123, Bairro Exemplo, Cidade Exemplo, Estado Exemplo",
            "atividade_principal": "Comércio varejista",
            "regime_de_apuracao": "Simples Nacional",
            "situacao_cadastral_vigente": "Ativa",
            "data_de_cadastramento": "2020-01-01",
            "data_de_consulta": "2023-10-01"
        }
        })
    response = client.get("/result/mock_task_id")
    assert response.status_code == 200
    assert response.json()['task_status'] == "completed"