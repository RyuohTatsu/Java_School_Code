import boto3
from decimal import Decimal

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')

def update_leaderboard(player_id, score):
    """
    Updates the leaderboard with the player's score.

    Args:
        player_id (str): The unique ID of the player.
        score (float): The score to be updated in the leaderboard.
    """
    table = dynamodb.Table('Leaderboard')
    try:
        # Convert the score to Decimal for compatibility with DynamoDB
        score = Decimal(str(score))
        
        # Retrieve the existing item for the player
        response = table.get_item(Key={'PlayerID': player_id})
        
        if 'Item' in response:
            item = response['Item']
            # Update player stats
            item['TimesPlayed'] += 1
            if score < item['BestLap']:
                item['BestLap'] = score
            table.put_item(Item=item)
            print(f"Leaderboard updated for {item['Name']}.")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error updating leaderboard: {e}")

def view_leaderboard():
    """
    Fetches and displays the leaderboard from the DynamoDB table. Lists all players
    with their PlayerID, Name, TimesPlayed, and BestLap.
    """
    table = dynamodb.Table('Leaderboard')
    try:
        # Scan the DynamoDB table to get all items
        response = table.scan()
        items = response['Items']
        # Display the leaderboard
        for item in items:
            print(f"PlayerID: {item['PlayerID']}, Name: {item['Name']}, TimesPlayed: {item['TimesPlayed']}, BestLap: {item['BestLap']}")
    except Exception as e:
        print(f"Error fetching leaderboard: {e}")