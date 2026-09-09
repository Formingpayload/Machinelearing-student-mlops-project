FROM python:3.12-slim-bookworm
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y awscli

RUN apt-get update && pip install -r requirements.txt

CMD ["python3", "app.py"]