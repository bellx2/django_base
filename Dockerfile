FROM debian:11-slim
#FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV RYE_HOME /root/.rye
ENV PATH ${RYE_HOME}/shims:${PATH}

RUN apt-get update && apt-get install -y curl
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash

WORKDIR /app
COPY . /app/
RUN rye sync

EXPOSE 8000
CMD [ "rye", "run", "server"]
