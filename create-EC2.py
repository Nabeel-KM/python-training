import boto3

# Create an EC2 client
client = boto3.client('ec2')

# Parameters
ami_id = 'ami-04a81a99f5ec58529'  # Replace with your AMI ID
instance_type = 't2.micro'        # Replace with your desired instance type
key_name = 'serverless_class'          # Replace with your key pair name
security_group_ids = ['sg-001beb6d32f40a979']  # Replace with your security group ID

# Create the instance
response = client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1
)

# Print instance details
for instance in response['Instances']:
    print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Public DNS: {instance['PublicDnsName']}")
