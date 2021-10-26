FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]