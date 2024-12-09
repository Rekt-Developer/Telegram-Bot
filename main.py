import os
import telebot
from flask import Flask, request
import requests

# Initialize Flask app
app = Flask(__name__)

# Get Bot Token from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Initialize Telebot
bot = telebot.TeleBot(BOT_TOKEN)

# Google Indexing API Function (Optional, requires Google Search Console setup)
def submit_to_google_index(url):
    """
    Submit a URL to Google for indexing
    Note: Requires Google Search Console API credentials
    """
    try:
        # This is a placeholder - you'll need to implement actual Google Indexing API logic
        index_url = "https://indexing.googleapis.com/v3/urlNotifications:publish"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "url": url,
            "type": "URL_UPDATED"
        }
        # Add your Google API authentication here
        response = requests.post(index_url, json=data, headers=headers)
        return response.json()
    except Exception as e:
        print(f"Indexing error: {e}")
        return None

# Handle channel post messages
@bot.message_handler(func=lambda message: True)
def handle_channel_post(message):
    """
    Process incoming messages and potentially index them
    """
    try:
        # Check if message is from a channel
        if message.chat.type == 'channel':
            # Extract message details
            channel_username = message.chat.username
            message_text = message.text or message.caption
            message_link = f"https://t.me/{channel_username}/{message.message_id}"
            
            # Optional: Submit to Google Index
            google_index_result = submit_to_google_index(message_link)
            
            # You can add logging or additional processing here
            print(f"New Channel Post: {message_link}")
    
    except Exception as e:
        print(f"Error processing message: {e}")

# Webhook route for Vercel
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    """
    Webhook endpoint to receive Telegram updates
    """
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

# Optional: Health check route
@app.route('/', methods=['GET'])
def home():
    return "Telegram Bot is running!", 200

# Set webhook (you'll call this once during setup)
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f'https://your-vercel-domain.vercel.app/{BOT_TOKEN}')

if __name__ == '__main__':
    set_webhook()
