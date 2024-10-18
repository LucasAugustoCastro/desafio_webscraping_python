FROM python:3.9-slim

ARG SERVICE=api

WORKDIR /app

EXPOSE 5000
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["fastapi", "run", "app/main.py", "--port", "5000"]