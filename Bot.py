import logging
from telegram.ext import Application, CommandHandler, MessageHandler
import uuid
import sqlite3  # Correct import (sqlite3 instead of sqlite4)
import asyncio

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace this with your bot token from BotFather
TOKEN = '7428161094:AAFFG0rb_uua_2v2SJcG2xF_tDDZTdD3dZA'

# Function to handle the /create command
async def create(update, context):
    user_id = update.message.from_user.id
    unique_id = str(uuid.uuid4())
    
    # Insert the UUID and Telegram user ID into the database
    conn = sqlite3.connect('app.db')  # Corrected sqlite4 to sqlite3
    cursor = conn.cursor()
    cursor.execute('INSERT INTO UserLink (telegram_user_id, uuid) VALUES (?, ?)', (user_id, unique_id))
    conn.commit()
    conn.close()

    # Respond with the generated link
    await update.message.reply_text(f'Your link is: http://localhost:5000/link/{unique_id}')

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Register the /create command handler
    application.add_handler(CommandHandler('create', create))

    application.run_polling(pool_timeout=3)
    
    # Run the bot until manually stopped
    #await application.idle()

if __name__ == '__main__':

    main()
