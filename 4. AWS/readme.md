# Crashcourse in AWS
## 1. Push the Model to S3
- Create S3 bucket
- Install AWS CLI

Modify your deploy script to download model from S3
you can use boto3 to download from S3 and load the model once
or you can use a bash script to download using aws cli

HINT: using S3 on Fargate will require a role to access S3 in Task Definition (Task role)
The Demo Web UI must run on port 80 and be publicly accessible
Push the Docker Image to ECR
Create a Fargate Spot Deployment on ECS
Share the link of the github repository that has the Dockerfile for above, and also your inference code
It should have instructions on how to run the Container ! 
NOTE: DO NOT EVER PUSH ANY OF YOUR AWS SECRETS TO GITHUB !
Share the image and tagname of the repo you pushed to AWS ECR
Submit your deployment ip address in Github Classroom which will test your deployment
try to keep your commits as less as possible <5 commits
before pushing test it