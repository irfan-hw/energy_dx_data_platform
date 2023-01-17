FROM python:3.7
ENV PYTHONUNBUFFERED 1

ADD . /work
WORKDIR /work

ADD requirements.txt /src/
RUN pip install -r requirements.txt
RUN apt-get install ca-certificates

EXPOSE 80
