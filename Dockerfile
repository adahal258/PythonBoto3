FROM ubuntu:latest

WORKDIR /aws_manager

COPY . .

RUN apt-get update && apt-get install -y python3 python3-pip python3-boto3

ENV NAME docker

CMD [ "python3", "aws_resource.py" ]