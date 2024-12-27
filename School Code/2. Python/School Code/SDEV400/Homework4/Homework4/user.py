import boto3
import uuid
from decimal import Decimal

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')

def register_user():
    """
    Registers a new user by storing their information in the DynamoDB table.
    """
    table = dynamodb.Table('Leaderboard')
    name = input("Enter your name: ")
    player_id = str(uuid.uuid4())  # Generate a unique player ID
    try:
        # Add the new user to the DynamoDB table
        table.put_item(
            Item={
                'PlayerID': player_id,
                'Name': name,
                'TimesPlayed': 0,
                'BestLap': Decimal('999999.99')  # Using a large number instead of Infinity
            }
        )
        # Display the name and player ID upon successful registration
        print(f"User {name} registered with PlayerID {player_id}.")
    except Exception as e:
        print(f"Error registering user: {e}")

def sign_in():
    """
    Signs in an existing user by verifying their name and player ID.
    """
    table = dynamodb.Table('Leaderboard')
    name = input("Enter your name: ")
    player_id = input("Enter your PlayerID: ")
    try:
        # Retrieve the user from the DynamoDB table
        response = table.get_item(Key={'PlayerID': player_id})
        if 'Item' in response and response['Item']['Name'] == name:
            user = response['Item']
            # Display a welcome message with the user's name and player ID
            print(f"Welcome back, {user['Name']} (PlayerID: {user['PlayerID']})!")
            return user['PlayerID']
        else:
            print("User not found or incorrect PlayerID. Please register first.")
            return None
    except Exception as e:
        print(f"Error signing in: {e}")
        return None