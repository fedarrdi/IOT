#FROM python:3.11-slim
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#CMD ["python", "app.py"]

FROM ubuntu
FROM debian:bullseye

RUN apt-get update && apt-get upgrade -y

RUN apt-get update && apt-get install -y python3

RUN apt install python3-pip -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python3 app.py

