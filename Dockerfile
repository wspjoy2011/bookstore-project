FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code




