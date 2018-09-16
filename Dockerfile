FROM python:3.6-slim-stretch

LABEL maintainer="Rosa Imantoro <rosaimantoro@gmail.com>"

RUN apt-get update \
    && apt-get install -y git vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./entrypoint.sh ./

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]