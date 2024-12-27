import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

def print_user_guide():
    """
    Fetches the user guide from the S3 bucket and prints its content to the terminal.
    """
    bucket_name = 'user.guide'  # Name of the S3 bucket
    object_key = 'user_guide.txt'  # Key of the object in the S3 bucket

    try:
        # Fetch the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        
        # Read the content of the object
        content = response['Body'].read().decode('utf-8')
        
        # Print the content to the terminal
        print(content)
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"Error fetching user guide: {e}")