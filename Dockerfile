FROM python:3.11-slim

WORKDIR /myapp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000