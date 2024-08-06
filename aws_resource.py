import boto3 as bt
import time

instance_ids = []

def get_aws_credentials():
    """Prompt the user for AWS credentials and return a boto3 client."""
    access_key = input("Enter your AWS Access Key: ")
    secret_key = input("Enter your AWS Secret Key: ")
    session_token = input("Enter your AWS Session Token (optional, press Enter to skip): ")
    region_name = input("Enter your AWS region (e.g., us-east-1): ")

    # Create a new boto3 session using the provided credentials
    if session_token:
        session = bt.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region_name
        )
    else:
        session = bt.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )
    
    return session.client('ec2')

def ec2_status():
    aws_ec2 = get_aws_credentials()
    aws_ec2_instances_info = aws_ec2.describe_instances()
    aws_ec2_reservations = aws_ec2_instances_info.get('Reservations')
    instance_count = 0
    print('Your cloud have following instances: ')
    for i in range(len(aws_ec2_reservations)):
        aws_ec2_available_instance = aws_ec2_reservations[i].get('Instances')
        for j in range(len(aws_ec2_available_instance)):
   
