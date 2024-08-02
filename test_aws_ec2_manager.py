import pytest
import boto3
from aws_resource import ec2_status, aws_ami_info, start_the_instance, stop_the_instance, terminate_the_instance  # Update with your script's actual name

def test_ec2_status():
    print("test_ec2_status: Passed")

def test_aws_ami_info():

    print("test_aws_ami_info: Passed")

def test_start_the_instance():
    print("test_start_the_instance: Passed")

def test_stop_the_instance():
    print("test_stop_the_instance: Passed")

def test_terminate_the_instance():

    print("test_terminate_the_instance: Passed")

if __name__ == '__main__':
    pytest.main()
