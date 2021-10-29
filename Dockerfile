FROM python:3.9.7-slim
ENV PYTHONUNBUFFERED=1
ARG SECRET_KEY
EXPOSE 8000
WORKDIR /app
COPY . /app

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]