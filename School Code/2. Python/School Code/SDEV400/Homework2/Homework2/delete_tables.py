import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

def delete_table(table_name):
    try:
        response = dynamodb.delete_table(TableName=table_name)
        print(f"Table {table_name} is being deleted.")
    except dynamodb.exceptions.ResourceNotFoundException:
        print(f"Table {table_name} does not exist.")
    except Exception as e:
        print(f"Error deleting table {table_name}: {e}")

# Delete the 'Sensors' table
delete_table('sensor_table')

# Delete the 'Courses' table
delete_table('Courses')