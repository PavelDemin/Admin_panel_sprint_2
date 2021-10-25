FROM python:latest
ENV SECRET_KEY="django-insecure-p@)y4usyttzv)y\=y)ars21ucbw2mqs#5ko50yy-\=7v50ar&8dm"
ENV POSTGRES_NAME="movies"
ENV POSTGRES_PASSWORD="qwerty123"
ENV POSTGRES_HOST="localhost"
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER="postgres"
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN chmod +x scripts/*

ENTRYPOINT ["scripts/docker-entrypoint.sh"]
