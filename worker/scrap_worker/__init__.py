from celery import Celery
from kombu import Queue
from dotenv import load_dotenv

load_dotenv()

from config import CeleryConfig

celery = Celery(__name__)
celery.config_from_object(CeleryConfig)