from celery import Celery
from config import BROKER_URL, RESULT_BACKEND

celery = Celery(__name__)
celery.config_from_object(
  {
    'broker_url': BROKER_URL,
    'result_backend': RESULT_BACKEND
  }
)
