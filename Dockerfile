FROM python:latest
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "localhost:8000", "config.wsgi:application"]
