FROM ubuntu:latest

WORKDIR /aws_manager

COPY . /aws_manager/

RUN apt-get update && apt-get install -y python3 python3-pip python3-boto3

ENV NAME docker

CMD [ "python3", "aws_resouce.py" ]pyth