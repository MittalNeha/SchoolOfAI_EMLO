# Crashcourse in AWS
## 1. Push the Model to S3
- Create S3 bucket
Create a EC2 instance and create demo_cifar10.py and Dockerfile
sudo apt update
sudo apt  install docker.io
- Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
- Create a IAM Policy to grand access to S3 and Roles
- 


Modify your deploy script to download model from S3
you can use boto3 to download from S3 and load the model once
or you can use a bash script to download using aws cli

HINT: using S3 on Fargate will require a role to access S3 in Task Definition (Task role)
The Demo Web UI must run on port 80 and be publicly accessible
Push the Docker Image to ECR
- Give ECR access to the EC2 instance by attaching the policies AmazonElasticContainerRegistryPublicFullAccess and AmazonEC2ContainerRegistryFullAccess


Create a Fargate Spot Deployment on ECS
Share the link of the github repository that has the Dockerfile for above, and also your inference code
It should have instructions on how to run the Container ! 
NOTE: DO NOT EVER PUSH ANY OF YOUR AWS SECRETS TO GITHUB !
Share the image and tagname of the repo you pushed to AWS ECR
Submit your deployment ip address in Github Classroom which will test your deployment
try to keep your commits as less as possible <5 commits
before pushing test it