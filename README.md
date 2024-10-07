Generate and send interactive Minesweeper games to Discord channels with ease!

## Description

This Python script creates customizable Minesweeper games and sends them directly to a Discord channel using webhooks. The game board is generated using Discord-compatible emojis and spoiler tags, allowing users to play the game right in the chat.

## Features

- Generates Minesweeper boards with customizable dimensions and mine count
- Automatically calculates numbers for adjacent mines
- Sends the generated game board to a Discord channel via webhook
- Uses spoiler tags for an interactive gameplay experience
- Notifies all users in the channel with @everyone mention

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/minesweeper-discord.git
   ```
2. Install the required library:
   ```
   pip install requests
   ```

## Usage

1. Open the script and replace `"[INSERT YOUR WEBHOOK URL HERE]"` with your actual Discord webhook URL.
2. Run the script:
   ```
   python minesweeper_discord.py
   ```
3. The script will generate a Minesweeper game and send it to your specified Discord channel.

## Running as a Cronjob

To automatically generate and send Minesweeper games at regular intervals, you can set up a cronjob. Here's how to do it on a Unix-based system:

1. Open your crontab file:
   ```
   crontab -e
   ```

2. Add a new line to schedule the script. For example, to run it every day at 3:00 PM:
   ```
   0 15 * * * /usr/bin/python3 /path/to/your/minesweeper_discord.py
   ```

   Adjust the timing and path as needed.

3. Save and exit the crontab editor.

Make sure the script has the necessary permissions to execute, and that the full path to both Python and your script are correctly specified.

Note: When running as a cronjob, ensure that any required environment variables (like API keys) are properly set or included in the script.

Important: Be mindful of Discord's rate limits and your server's rules when setting up automated posts.

## Customization

You can customize the Minesweeper game by modifying the parameters in the `generate_minesweeper()` function call:

- `rows`: Number of rows in the game board (default: 9)
- `columns`: Number of columns in the game board (default: 9)
- `mines`: Number of mines to place on the board (default: 10)
- `emoji`: The emoji to use for mines (default: '💣')

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/daronjniemeyer/sweeperbot-discord/issues).

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

Please use this script responsibly and in accordance with Discord's terms of service and community guidelines. Avoid spamming channels or users with excessive game boards.
