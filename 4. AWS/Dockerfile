# our base image
FROM zironycho/pytorch:1120-cpu-py38

ENV GRADIO_SERVER_PORT 80

# set working directory inside the image
WORKDIR /

# copy our requirements
COPY requirements.txt requirements.txt


# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# copy this folder contents to image
COPY demo_cifar10.py .
# COPY model.script.pt .
# COPY cifar10_classes.json .
# COPY pyproject.toml .

# tell the port number the container should expose
EXPOSE 80

# run the application
ENTRYPOINT [ "python3", "demo_cifar10.py"]
# CMD ["bash"]