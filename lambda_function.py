import json
import boto3
from s3_operations import upload_to_s3
from dynamodb_operations import store_in_dynamodb

def lambda_handler(event, context):
    # Process IoT data from the event
    data = json.loads(event['body'])
    
    # Transform data (example: extracting relevant fields)
    transformed_data = {
        "device_id": data['device_id'],
        "timestamp": data['timestamp'],
        "value": data['value'] * 1.25  # Sample transformation
    }
    
    # Upload transformed data to S3
    upload_to_s3(transformed_data)
    
    # Store metadata in DynamoDB
    store_in_dynamodb(transformed_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully!')
    }
