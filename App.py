from flask import Flask
import sqlite3

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return 'Please use the bot to get a link.'

# Link Route
@app.route('/link/<uuid>',methods=['GET'])
def show_user_id(uuid):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # Query the database to get the user by UUID
    cursor.execute('SELECT telegram_user_id FROM UserLink WHERE uuid=?', (uuid,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return f'The Telegram user ID is: {user[0]}'
    else:
        return 'Invalid UUID!'

if __name__ == '__main__':
    app.run(port=5000)

