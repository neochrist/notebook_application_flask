FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./notebook_application/ .
COPY /entrypoint.sh /
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y default-mysql-client

ENTRYPOINT ["/entrypoint.sh"]