FROM python:3.6-slim-stretch

LABEL maintainer="Rosa Imantoro <rosaimantoro@gmail.com>"

RUN apt-get update \
    && apt-get install -y git vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir app

COPY ./app/* entrypoint.sh ./app/

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]