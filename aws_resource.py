'''
Author: Aashutosh Dahal

Created: 7/29/2024

This program will load up all the aws services running/ stopped or any computing resources attached with the organization
Will count the instances available:
list available instance-id and allow user to choose.
Will run my instance specified,stop or terminate. Right now I only have one instances but can be modified to run all at once or stop all at once.

'''
import boto3 as bt
import time

instance_ids = []

def get_aws_credentials():
    """Prompt the user for AWS credentials and return a boto3 client."""
    access_key = input("Enter your AWS Access Key: ")
    secret_key = input("Enter your AWS Secret Key: ")
    session_token = input("Enter your AWS Session Token (optional, press Enter to skip): ")

    # Create a new boto3 session using the provided credentials
    if session_token:
        session = bt.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token
        )
    else:
        session = bt.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
    
    return session.client('ec2')

def ec2_status():
    aws_ec2_instances_info = aws_ec2.describe_instances()
    aws_ec2_reservations = aws_ec2_instances_info.get('Reservations')
    instance_count = 0
    print('Your cloud have following instances: ')
    for i in range(len(aws_ec2_reservations)):
        aws_ec2_available_instance = aws_ec2_reservations[i].get('Instances')
        for j in range(len(aws_ec2_available_instance)):
            print('########################################################')
            aws_ec2_ins = aws_ec2_available_instance[j]
            aws_ec2_instanceId = aws_ec2_ins.get('InstanceId')
            instance_ids.append(aws_ec2_instanceId)
            print(f'{instance_count + 1}. {aws_ec2_ins.get("Tags")[0].get("Value")}: {aws_ec2_instanceId}')
            print()
            print(f'\t Arch: {aws_ec2_ins.get("InstanceType")} ')
            if aws_ec2_ins.get('State').get('Name') == 'running':
                print(f'Status: Running')
                print(f'Public Ip: {aws_ec2_ins.get("PublicIpAddress")} Private Ip: {aws_ec2_ins.get("PrivateIpAddress")}')
            else:
                print(str(aws_ec2_ins.get('State').get('Name')))
            print('########################################################\n\n')
            instance_count += 1
    return aws_ec2

def aws_ami_info():
    aws_ec2 = ec2_status()
    user_input = input("Do you want to perform an action[Y/N]? ")
    while user_input not in ['Y', 'N']:
        print("Please press Y or N")
        user_input = input("Do you want to perform an action[Y/N]? ")
    if user_input == 'Y':
        aws_compute_action(aws_ec2)
    else:
        print('Thank You!')
        # to get the updated status of your aws_instance info
        time.sleep(10)
        ec2_status()

def aws_compute_action(aws_ec2):
    user_action = input("Do you want to start (s), stop(S), Terminate(T) or Exit(E) ? ")
    while user_action not in ['s', 'S', 'T', 'E']:
        print("Accepted: s, S, T or E")
        user_action = input("Do you want to start(s), stop(S), Terminate(T) or Exit(E) ? ")
    if user_action == 's':
        start_the_instance(aws_ec2)
    elif user_action == 'S':
        stop_the_instance(aws_ec2)
    elif user_action == 'T':
        terminate_the_instance(aws_ec2)
    else:
        print("Exiting...........")
        time.sleep(2)
        ec2_status()

def start_the_instance(aws_ec2):
    instance_id = []
    while True:
        try:
            ins_num = int(input('How many instance you want to start? '))
            break
        except ValueError:
            print("The input is not string ONLY NUMBERS: ")
            continue 
        
    if ins_num > len(instance_ids):
        print(f"You only have {len(instance_ids)} in your cloud. ")
        print(f"Assuming you want to start {len(instance_ids)} instances")
        ins_num = len(instance_ids)
        
    for i in range(ins_num):
        instance_id_info = input('Enter instance id (Please verify it): ')
        if instance_id_info in instance_ids:
            instance_id.append(instance_id_info)
        else:
            print("Please verify instance-id correctly")
            aws_ami_info()
    print(instance_id)
    aws_ec2.start_instances(InstanceIds=instance_id)
    print("\n\nStarting........................\n\n")
    time.sleep(40)
    aws_ami_info()

def stop_the_instance(aws_ec2):
    instance_id = []
    while True:
        try:
            ins_num = int(input('How many instance you want to stop? '))
            break
        except ValueError:
            print("The input is not string ONLY NUMBERS: ")
            continue 

    if ins_num > len(instance_ids):
        print(f"You only have {len(instance_ids)} in your cloud. ")
        print(f"Assuming you want to stop {len(instance_ids)} instances")
        ins_num = len(instance_ids)
        
    for i in range(ins_num):
        instance_id_info = input('Enter instance id (Please verify it): ')
        if instance_id_info in instance_ids:
            instance_id.append(instance_id_info)
        else:
            print("Please verify instance-id correctly")
            aws_ami_info()
    print(instance_id)
    aws_ec2.stop_instances(InstanceIds=instance_id)
    print("\n\nStopping........................\n\n")
    time.sleep(20)
    aws_ami_info()

def terminate_the_instance(aws_ec2):
    instance_id = []
    while True:
        try:
            ins_num = int(input('How many instance you want to terminate? '))
            break
        except ValueError:
            print("The input is not string ONLY NUMBERS: ")
            continue 
    if ins_num > len(instance_ids):
        print(f"You only have {len(instance_ids)} in your cloud. ")
        print(f"Assuming you want to terminate {len(instance_ids)} instances")
        ins_num = len(instance_ids)
        
    for i in range(ins_num):
        instance_id_info = input('Enter instance id (Please verify it): ')
        if instance_id_info in instance_ids:
            instance_id.append(instance_id_info)
        else:
            print("Please verify instance-id correctly")
            aws_ami_info()
    print(instance_id)
    aws_ec2.terminate_instances(InstanceIds=instance_id)
    print("\n\nTerminating........................\n\n")
    time.sleep(5)
    aws_ami_info()

if __name__ == '__main__':
    aws_ec2 = get_aws_credentials()
    aws_ami_info()
