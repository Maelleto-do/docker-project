# DockerFile, Image (template for running containers), Container (actual running process)

FROM python:3.8


ADD main.py .

# install dependecies
RUN pip install pennylane

CMD ["python", "./main.py"]