# Ethos

This is a simple Discord bot that allows users to check in daily, tracks their check-in count, and displays a leaderboard.

## Features

-   **Daily Check-in:** Users can check in once per day using the `/check_in` command.
-   **Yearly Check-in Count:** Users can see their total check-ins for the year using the `/yearly_check_in` command.
-   **Leaderboard:** Displays a leaderboard of users with the most check-ins using the `/leaderboard` command.
-   **Fun Command:** Includes a fun command `/ian_is_handsome`.

## Prerequisites

-   Python 3.6+
-   Discord account and server
-   A Discord bot token
-   `discord.py` library
-   `python-dotenv` library

## Setup

1.  **Install Python Dependencies:**

    ```bash
    pip install discord.py python-dotenv
    ```

2.  **Create a Discord Bot:**

    -   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    -   Create a new application and then create a bot within that application.
    -   Copy the bot token.

3.  **Create a `.env` File:**

    -   Create a `.env` file in the same directory as your Python script.
    -   Add your bot token to the `.env` file like this:

    ```
    API_TOKEN=YOUR_BOT_TOKEN
    ```

    -   Replace `YOUR_BOT_TOKEN` with your actual bot token.

4.  **Invite the Bot to Your Server:**

    -   In the Discord Developer Portal, go to the "OAuth2" tab.
    -   In the "Scopes" section, select "bot" and "applications.commands".
    -   In the "Bot Permissions" section, select the permissions your bot needs (e.g., "Send Messages", "Read Message History").
    -   Copy the generated URL and paste it into your browser.
    -   Select the server you want to add the bot to and authorize it.

## Running the Bot

1.  **Save the Python Script:**

    -   Save the provided Python code as a `.py` file (e.g., `checkin_bot.py`).

2.  **Run the Bot:**

    -   Open a terminal or command prompt.
    -   Navigate to the directory where you saved the script and the `.env` file.
    -   Run the script using Python:

    ```bash
    python checkin_bot.py
    ```

3.  **Use the Commands:**

    -   Once the bot is running, you can use the following commands in your Discord server:
        -   `/check_in`: Check in for the day.
        -   `/yearly_check_in`: See your total check-ins for the year.
        -   `/leaderboard`: View the check-in leaderboard.
        -   `/ian_is_handsome`: Enjoy a fun message.

## How it Works

-   The bot uses `discord.py` to interact with the Discord API.
-   The `dotenv` library is used to load the bot token from the `.env` file.
-   The bot stores user check-in data in a `checkins.json` file.
-   The bot uses slash commands (application commands) for user interaction.
-   The bot tracks the last check-in date and the yearly check-in count for each user.

## File Structure
