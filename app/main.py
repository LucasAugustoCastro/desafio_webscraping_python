from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from scrape_api.routes import scrape

app = FastAPI()
app.include_router(scrape.router)
