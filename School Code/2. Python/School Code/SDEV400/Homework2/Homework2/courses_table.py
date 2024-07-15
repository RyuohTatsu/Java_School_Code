import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create DynamoDB table
table_name = 'Courses'

try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'CourseID',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'CourseID',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"Table {table_name} created successfully!")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists.")