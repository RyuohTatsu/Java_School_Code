import random

# Define optimal braking distances (in feet) and their corresponding speeds (in mph)
optimal_braking_distances = [200, 150, 100, 120, 180, 160]  # Optimal distances for each corner
speeds = [160, 110, 70, 90, 160, 130]  # Speeds for each corner, ranging from 70 mph to 160 mph

def Welcome():
    """
    Displays the welcome message and game instructions.
    """
    print("\nWelcome to the Lap Time Calculator Game!")
    print("You will navigate through a lap with 6 corners.")
    print("For each corner, input a braking distance between 200 feet and 50 feet.")
    print("The speed is fixed for each corner, but varies between corners.")
    print("Try to brake at the optimal distance to achieve the best lap time.")
    print("If you brake too early or too late, your lap time will increase.")
    print("\nThe optimal lap time is 1 minute and 30 seconds.")

def get_braking_distance(corner_number, speed, optimal_distance):
    """
    Prompts the user for the braking distance for a specific corner.

    Args:
        corner_number (int): The corner number for which the braking distance is being input.
        speed (int): The speed for the current corner.
        optimal_distance (int): The optimal braking distance for the current corner.

    Returns:
        float: The braking distance input by the user.
    """
    while True:
        try:
            print(f"\nYou are racing towards corner number {corner_number} at a speed of {speed} mph. Which braking marker will you choose?")
            brk_dis = float(input(f'Enter your braking distance between 50 and 200 feet: '))
            if 50 <= brk_dis <= 200:
                return brk_dis
            else:
                print("Invalid input. Please enter a number between 50 and 200.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_lap_time(brk_distances):
    """
    Calculates the total lap time based on the braking distances provided.

    Args:
        brk_distances (list): List of braking distances for each corner.

    Returns:
        float: The total lap time.
    """
    # Optimal braking distances for each corner
    optimal_brk_distances = [150, 130, 180, 120, 170, 140]
    
    # Initialize total lap time to the optimal lap time (90 seconds)
    total_lap_time = 90.0

    for i in range(6):
        brk_dis = brk_distances[i]
        optimal_brk_dis = optimal_brk_distances[i]
        if brk_dis < optimal_brk_dis:
            total_lap_time += 0.2 * ((optimal_brk_dis - brk_dis) / 20)
        elif brk_dis > optimal_brk_dis:
            total_lap_time += 0.3 * ((brk_dis - optimal_brk_dis) / 20)

    return total_lap_time

def display_output(lap_time):
    """
    Displays the lap time and the result.

    Args:
        lap_time (float): The calculated lap time.
    """
    print("\nYour lap time is:", round(lap_time, 2), "seconds")
    if lap_time == 90.0:
        print("Congratulations! You achieved the optimal lap time!")
    elif lap_time < 90.0:
        print("Great job! You finished the lap faster than the optimal time.")
    else:
        print("Good effort! Try again to improve your lap time.")

def start_game(player_id=None):
    """
    Starts the game, prompts for braking distances for each corner, calculates the lap time,
    and updates the leaderboard if a player is signed in.

    Args:
        player_id (str, optional): The unique ID of the player if signed in. Defaults to None.
    """
    Welcome()
    brk_distances = []
    
    # Prompt user for braking distances at each corner
    for corner in range(1, 7):  # Corners 1 to 6
        speed = speeds[corner - 1]  # Speed for the current corner
        optimal_distance = optimal_braking_distances[corner - 1]  # Optimal distance for the current corner
        brk_distances.append(get_braking_distance(corner, speed, optimal_distance))
    
    # Calculate and display the lap time
    lap_time = calculate_lap_time(brk_distances)
    display_output(lap_time)

    # Update the leaderboard if the user is signed in
    if player_id:
        from leaderboard import update_leaderboard
        update_leaderboard(player_id, lap_time)