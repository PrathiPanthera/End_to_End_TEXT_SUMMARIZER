FROM python:3.11-slim-bookworm

RUN apt-get update \
    && apt-get install -y awscli \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 2122

CMD ["python", "app.py"]