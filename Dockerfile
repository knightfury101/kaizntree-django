# pull official base image
FROM python:3.8.13-slim-buster

# set work directory
WORKDIR /kaizntree_backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc rabbitmq-server
RUN pip install -U pip setuptools wheel ruamel.yaml ruamel.yaml.clib==0.2.6 celery
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN sed -i 's/\r$//g' /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
RUN chown -R "$USER":www-data /kaizntree_backend/ && chmod -R 755 /kaizntree_backend/

# copy project
COPY . .

# ENTRYPOINT ["/docker-entrypoint.sh"]