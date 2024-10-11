import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print("Bucket created successfully")

def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb') # Read Binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")


bucket_name = "python-test-devops-nab"
file_name = "/home/nabeel-sarfraz/python-training/backups/backup_2024-09-18 18:30:00.250381.tar.gz"
key_name = "my-backup.tar.gz"

upload_backup(s3,file_name,bucket_name,key_name)
# create_bucket(s3, bucket_name)

# show_buckets(s3)