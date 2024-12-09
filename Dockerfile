FROM python:3.11

RUN apt update && apt upgrade -y

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]
