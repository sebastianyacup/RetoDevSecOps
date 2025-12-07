FROM python:3.14.1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
