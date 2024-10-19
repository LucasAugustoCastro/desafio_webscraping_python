FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    firefox-esr \
    jq \
    && rm -rf /var/lib/apt/lists/*

RUN GECKO_DRIVER_VERSION=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest | jq -r '.tag_name') && \
    wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ && \
    rm /tmp/geckodriver.tar.gz

ENV DISPLAY=:99

WORKDIR /worker

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /worker

CMD ["celery", "-A", "scrap_worker.tasks", "worker", "--loglevel=info"]
