import boto3
import json

s3 = boto3.client('s3')
bucket_name = 'parkz-data-storage-1'

def upload_to_s3(data):
    key = f"data/{data['device_id']}/{data['timestamp']}.json"
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
