FROM python:slim-bullseye

COPY . .

RUN python3 main.py