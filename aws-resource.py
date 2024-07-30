'''
Author: Aashutosh Dahal

Created: 7/29/2024

This program will load up all the aws services running/ stopped or any computing resources attached with the organization
Will count the instances available:
list available instance-id and allow user to choose.
Will run my instance specified. Right now I only have one instances but can be modified to run all at once or stop all at once.
List aws resources: S3 bucket, IAM user, billing, lambda...

'''
import boto3 as bt
import time


def ec2_status():
    aws_ec2 = bt.client('ec2')
    aws_ec2_instances_info = aws_ec2.describe_instances()
    aws_ec2_reservations = aws_ec2_instances_info.get('Reservations')
    instance_count = 0
    print('Your cloud have following instances: ')
    for i in range(0, len(aws_ec2_reservations)):
        aws_ec2_availabe_instance = aws_ec2_reservations[i].get('Instances')
        for j in range(0, len(aws_ec2_availabe_instance)):
            print('########################################################')
            aws_ec2_ins = aws_ec2_availabe_instance[j]
            print(str(instance_count+1) + '. ' + str(aws_ec2_ins.get('InstanceId')))
            print(f'\t Arch: {aws_ec2_ins.get('InstanceType')} ')
            if((aws_ec2_ins.get('State')).get('Name')=='running'):
                print('Status: Running')
            else:
                print(str((aws_ec2_ins.get('State')).get('Name')))
            print(f'########################################################\n\n')
            instance_count += 1
    return aws_ec2
            
def aws_ami_info():
    aws_ec2 = ec2_status()
    user_input = input("Do you want to perform an action[Y/N]? ")
    while (user_input !='Y' and user_input != 'N'):
        print("Please press Y or N")
        user_input = input("Do you want to perform an action[Y/N]? ")
    if user_input=='Y':
        aws_compute_action(aws_ec2)
    else:
        print('Thank You!')
        time.sleep(3)
        ec2_status()
        
def aws_compute_action(aws_ec2):
    user_action = input("Do you want to start (s), stop(S), Terminate(T) or Exit(E) ? ")
    while (user_action != 's' and user_action !='S' and user_action != 'T' and user_action != 'E'):
        print("Accepted: S, T or E")
        user_action = input("Do you want to start(s), stop(S), Terminate(T) or Exit(E) ? ")
    if user_action == 's':
        start_the_instance(aws_ec2)
    elif user_action == 'S':
        stop_the_instance(aws_ec2)
    # elif user_action == 'T':
    #     terminate_the_instance()
    else:
        print("Exiting...........")
        time.sleep(2)
        ec2_status()
        

def start_the_instance(aws_ec2):
    instance_id = []
    ins_num = int(input('How many instance you want to start? '))
    for i in range(0, ins_num):
        instance_id_info = input('Enter instance id (Please verify it): ')
        instance_id.append(instance_id_info)
    print(instance_id)
    aws_ec2.start_instances(InstanceIds= instance_id)
    print("\n\nStarting........................\n\n")
    time.sleep(5)
    aws_ami_info()
        
def stop_the_instance(aws_ec2): 
    instance_id = []
    ins_num = int(input('How many instance you want to stop? '))
    for i in range(0, ins_num):
        instance_id_info = input('Enter instance id (Please verify it): ')
        instance_id.append(instance_id_info)
    print(instance_id)
    aws_ec2.stop_instances(InstanceIds = instance_id)
    print("\n\nStopping........................\n\n")
    time.sleep(5)
    aws_ami_info()
    
# def terminate_the_instance():     

#     print(aws_ec2_instances_info)
    
#     print(f'There are {len(aws_ec2_reservations)} types of virtual server')
#     print('Here are the list: ')
#     # for i in range (0, len(aws_ec2_instances_info)):
        

if __name__ == '__main__':
    aws_ami_info()
 