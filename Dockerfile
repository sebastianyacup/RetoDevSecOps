FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "wait_for_db.py", "upbasededatos", "5432", "flask", "db", "upgrade"]

EXPOSE 5000
