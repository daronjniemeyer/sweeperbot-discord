import requests
import random

# Set your Discord webhook URL here
webhook_url = "[INSERT YOUR WEBHOOK URL HERE]"

def generate_minesweeper(rows=9, columns=9, mines=10, emoji='💣'):
    # Generate a Minesweeper board with specified dimensions and number of mines.

    # Create an empty board with zeros
    board = [[0 for col in range(columns)] for row in range(rows)]

    # Place mines randomly on the board
    mine_count = 0
    while mine_count < mines:
        x, y = random.randint(0, rows - 1), random.randint(0, columns - 1)
        if board[x][y] != -1:  # Check if the cell is not already a mine
            board[x][y] = -1  # -1 represents a mine
            mine_count += 1

    # Calculate numbers for adjacent mines
    for x in range(rows):
        for y in range(columns):
            if board[x][y] == -1:  # Skip mine cells
                continue
            # Count surrounding mines
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and board[nx][ny] == -1:
                        board[x][y] += 1

    # Map numbers and mines to emoji representation
    emojis = {
        -1: emoji,
        0: ':blue_square:',  # Blue square emoji
        1: ':one:',          # Number 1 emoji
        2: ':two:',          # Number 2 emoji
        3: ':three:',        # Number 3 emoji
        4: ':four:',         # Number 4 emoji
        5: ':five:',         # Number 5 emoji
        6: ':six:',          # Number 6 emoji
        7: ':seven:',        # Number 7 emoji
        8: ':eight:'         # Number 8 emoji
    }

    # Convert board to a string format
    result = []
    for row in board:
        new_row = [f"||{emojis[cell]}||" for cell in row]  # Use spoiler tags for each cell
        result.append(' '.join(new_row))  # Join each row with a space

    return '\n'.join(result)  # Join all rows with a newline

def send_dc_message(webhook_url, message):
    # Send a message to a Discord channel via a webhook.
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)  # Use JSON to send the data
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Example usage
minesweeper_board = "@everyone \n\n" + generate_minesweeper()

send_dc_message(webhook_url, minesweeper_board)  # Send the board to Discord
