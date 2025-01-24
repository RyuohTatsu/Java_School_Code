import requests
from bs4 import BeautifulSoup

# URL of the Google Doc (your shared document)
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'

# Fetch the content of the Google Doc page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table (assuming the first table contains the necessary data)
    table = soup.find('table')
    
    # Extract rows from the table
    rows = table.find_all('tr')
    
    # Create a dictionary to hold the character positions
    character_positions = {}
    
    # Loop through rows and extract data, skipping the header row
    for row in rows[1:]:  # Start from the second row to skip the header
        cols = row.find_all('td')
        
        # Check if row has three columns
        if len(cols) == 3:
            try:
                x_coord = int(cols[0].text.strip())  # X-coordinate
                character = cols[1].text.strip()  # Character
                y_coord = int(cols[2].text.strip())  # Y-coordinate
                
                # Store the character at its (x, y) position in the dictionary
                if y_coord not in character_positions:
                    character_positions[y_coord] = {}
                character_positions[y_coord][x_coord] = character
            except ValueError:
                # If conversion fails, skip this row
                continue
    
    # To determine the grid size, find the max x and y values
    max_x = max(max(row.keys()) for row in character_positions.values())  # Max x-coordinate
    max_y = max(character_positions.keys())  # Max y-coordinate
    
    # Create a grid with the characters in the correct positions
    grid = []
    
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            # If there is a character at the (x, y) position, add it, otherwise add a space
            char = character_positions.get(y, {}).get(x, ' ')
            
            # Replace unsupported characters with a placeholder (e.g., '?')
            row.append(char if char.isprintable() else '?')
        
        grid.append(row)
    
    # Print the grid to a text file
    with open("output_grid.txt", "w", encoding="utf-8") as file:
        for row in grid:
            file.write(' '.join(row) + '\n')
    
    print("Grid has been written to 'output_grid.txt'")
else:
    print(f"Failed to fetch the document. Status code: {response.status_code}")
