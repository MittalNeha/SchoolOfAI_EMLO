# our base image
FROM python:3.9-slim-buster

ENV GRADIO_SERVER_PORT 8080

# set working directory inside the image
WORKDIR /

# copy our requirements
COPY docker-requirements.txt requirements.txt


# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# copy this folder contents to image
COPY demo_cifar10.py .
COPY model.script.pt .
COPY cifar10_classes.json .
# COPY pyproject.toml .

# tell the port number the container should expose
EXPOSE 8080

# run the application
ENTRYPOINT [ "python3", "demo_cifar10.py"]
# CMD ["sh"]