FROM python:3.11

RUN mkdir -p /code
ADD . /code

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --progress-bar off