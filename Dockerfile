# This program will make the whole project as Docker image
FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "main.py", "app.py"]