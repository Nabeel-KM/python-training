import boto3

# Create an S3 resource
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

client = boto3.client('ec2')

# Describe instances
response = client.describe_instances(
 # Set to True to test without making the request
)

# Print out the response
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['InstanceType'], instance['State']['Name'])