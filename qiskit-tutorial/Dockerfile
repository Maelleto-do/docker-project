FROM debian:latest
FROM python:latest

RUN pip install --upgrade pip
RUN pip install matplotlib
RUN pip install numpy
RUN pip install qiskit
RUN pip install pylatexenc

# RUN apt update
# RUN apt install wget -y
# RUN wget build-essential libreadline-gplv2-dev libncursesw5-dev \
# RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
# RUN tar xzf Python-3.9.1.tgz
# RUN cd Python-3.9.1
# RUN /configure --enable-optimizations
# RUN make -j 2
# RUN sudo make alt install

RUN mkdir -p /usr/dockerData
RUN chmod 744 /usr/dockerData

WORKDIR /usr/dockerData

COPY qiskit_program.py ./


CMD [ "python" , "./qiskit_program.py" ] 