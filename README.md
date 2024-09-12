# Aage_bot
Certainly! Here's a README file for your GitHub repository based on the project details you provided earlier. Feel free to adjust any specific details as needed.

---

# Aage Bot

## Overview

Aage Bot is a project that combines a Telegram bot with a web server, using SQLite for data storage. The bot allows users to generate unique links that, when visited, display their Telegram user ID. The project includes both the bot code and the web server code.

## Features

- **Telegram Bot**:
  - `/create`: Generates a new UUID4, creates an entry in the database, and returns a unique link to the user.

- **Web Server**:
  - `/`: Displays a message directing users to use the bot.
  - `/link/{id}`: Displays the user's Telegram user ID based on the UUID provided in the link.

## Requirements

- Python 3.x
- SQLite
- `python-telegram-bot` library
- `flask` library

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/euphoricfenix/Aage_bot.git
   cd Aage_bot
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**

   Update the `TOKEN` variable in `bot.py` with your Telegram Bot API key.

   ```python
   TOKEN = 'YOUR_TELEGRAM_BOT_API_KEY'
   ```

5. **Initialize the Database**

   Ensure that `database.py` has been run to create the necessary SQLite database and table.

   ```bash
   python database.py
   ```

6. **Run the Web Server**

   ```bash
   python app.py
   ```

7. **Run the Telegram Bot**

   ```bash
   python bot.py
   ```

## Usage

1. **Start the Bot**:
   - Open your Telegram app and search for your bot by its username.
   - Use the `/create` command to generate a unique link.

2. **Visit the Generated Link**:
   - Click on the link provided by the bot. It will take you to a webpage displaying your Telegram user ID.
