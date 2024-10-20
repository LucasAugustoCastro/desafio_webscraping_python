# Desafio de Scraping com FastAPI e Celery

Este projeto é uma aplicação de scraping que utiliza FastAPI para a API e Celery para tarefas assíncronas. A aplicação é containerizada usando Docker e Docker Compose.

## Estrutura do Projeto
```
├── README.md
├── app
│   ├── Dockerfile
│   ├── example.env
│   ├── main.py
│   ├── requirements.txt
│   ├── scrape_api
│   │   ├── celery_app.py
│   │   ├── config.py
│   │   ├── routes
│   │   │   └── scrape.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── result_scrape.py
│   │   │   └── scrape.py
│   │   └── tasks.py
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       └── test_scrape.py
├── docker-compose.yml
└── worker
    ├── Dockerfile
    ├── example.env
    ├── requirements.txt
    ├── scrap_worker
    │   ├── __init__.py
    │   ├── config.py
    │   ├── scrape_sintegra.py
    │   └── tasks.py
    ├── teste.py
    └── tests
        ├── __init__.py
        ├── conftest.py
        ├── mock_data
        │   └── cnpj_page.html
        └── test_scrape_sintegra.py

```
## Pré-requisitos
- Python 3.12+
- Docker e Docker Compose

## Como Executar o Projeto
### Passo 1: Clonar Repositorio
```
git clone https://github.com/LucasAugustoCastro/desafio_webscraping_python.git
cd desafio_webscraping_python
```

### Passo 2: Configurar Variáveis de Ambiente
Crie os arquivos .env baseados nos arquivos de exemplo fornecidos:
```
cp app/example.env app/.env
cp worker/example.env worker/.env
```
Preencha as variáveis conforme necessário.

### Passo 3: Construir e Iniciar os Containers
```
docker-compose up --build
```

### Passo 4: Acessar a Aplicação
A API estará disponível em http://localhost:5000.

### Passo 5: Executar Tarefas de Scraping
#### Exemplo de Execução de Tarefas de Scraping
Para executar uma tarefa de scraping, você pode usar o seguinte comando curl:

```bash
curl -X POST "http://localhost:5000/scrape" -H "Content-Type: application/json" -d '{"cnpj": "Um numero de CNPJ"}'
```
Isso enviará uma solicitação POST para a API com a URL que você deseja fazer o scraping.

#### Exemplo de Verificação de Status de Tarefa

Para verificar o status de uma tarefa de scraping, você pode usar o seguinte comando curl, substituindo `<task_id>` pelo ID da tarefa retornado na resposta da solicitação de scraping:

```bash
curl "http://localhost:5000/status/<task_id>"
```
Isso retornará o status atual da tarefa de scraping.

## Rodando o Projeto Sem Docker
### Passo 1: Criar o Ambiente Virtual
```
python -m venv venv
```
### Passo 2: Ativar o Ambiente Virtual
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS/Linux:
  ```
  source venv/bin/activate
  ```
### Passo 3: Instalar as Dependências
```
pip install -r app/requirements.txt
pip install -r worker/requirements.txt
```

## Testes
### Rodando os Testes
Certifique-se de que o ambiente virtual esteja ativo, as dependencias instaladas e rode os testes:
```
pytest worker/tests
pytest app/tests
```
