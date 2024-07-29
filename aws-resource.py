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

aws_ec2 = bt.client('ec2')
aws_ec2_instances_info = aws_ec2.describe_instances()
aws_ec2_reservations = aws_ec2_instances_info.get('Reservations')


def aws_ami_info():
    instance_count = 0
    print('Your cloud is running following instances: ')
    for i in range(0, len(aws_ec2_reservations)):
        aws_ec2_availabe_instance = aws_ec2_reservations[i].get('Instances')
        for j in range(0, len(aws_ec2_availabe_instance)):
            print('########################################################')
            print(str(instance_count+1) + '. ' + str(aws_ec2_availabe_instance[j].get('InstanceId')))
            print(f'\t Arch: {aws_ec2_availabe_instance[j].get('InstanceType')} ')
            print(f'########################################################\n\n')
            instance_count += 1
    
# def aws_compute_info():

#     print(aws_ec2_instances_info)
    
#     print(f'There are {len(aws_ec2_reservations)} types of virtual server')
#     print('Here are the list: ')
#     # for i in range (0, len(aws_ec2_instances_info)):
        

if __name__ == '__main__':
    aws_ami_info()
 