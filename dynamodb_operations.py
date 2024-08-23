import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'IoTData'
table = dynamodb.Table(table_name)

def store_in_dynamodb(data):
    table.put_item(Item=data)
