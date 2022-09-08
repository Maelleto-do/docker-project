FROM debian:latest
FROM python:3.8-slim

RUN pip install pennylane --upgrade

RUN mkdir -p /usr/dockerData
RUN chmod 744 /usr/dockerData

WORKDIR /usr/dockerData

COPY pennylane_program.py ./


CMD [ "python" , "./pennylane_program.py" ] 