FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "until pg_isready -h db -U ccss; do echo 'Waiting for Postgres...'; sleep 1; done && python manage.py runserver 0.0.0.0:8000"]
