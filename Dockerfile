FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip && pip install tornado

EXPOSE 8080

# https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
ENV PYTHONUNBUFFERED 1

COPY './main.py' main.py

CMD ./main.py
