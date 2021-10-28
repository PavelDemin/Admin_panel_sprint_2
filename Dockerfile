FROM python:latest
ENV PYTHONUNBUFFERED=1
ARG SECRET_KEY

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]