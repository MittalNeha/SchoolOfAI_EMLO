# our base image
FROM python:3.9-slim

# set working directory inside the image
WORKDIR /

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy this folder contents to image
COPY . .

# tell the port number the container should expose
EXPOSE 5000

# run the application
# CMD [ "python3", "pytorch-image-models/inference.py", "../test_images", "--model mobilenetv3_large_100"] 
# CMD [ "python3", "main.py", "test_images", "--num-gpu", "0"] 
# python3 main.py ../test_images --model resnet18 --num-gpu 0
ENTRYPOINT ["python", "main.py"]
