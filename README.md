# Telegram Channel Indexing Bot

## Overview
This Telegram bot is designed to automatically index channel posts from the @LikhonAPI channel and potentially submit them to Google for indexing.

## Features
- Receive and process Telegram channel posts
- Optional Google Indexing integration
- Deployment-ready for Vercel

## Prerequisites
- Python 3.8+
- Telegram Bot Token
- Vercel Account

## Setup Instructions

### 1. Create Vercel Project
1. Fork this repository
2. Import the project to Vercel

### 2. Set Environment Variables
In Vercel Project Settings, add:
- `TELEGRAM_BOT_TOKEN`: Your Telegram Bot Token
- `GOOGLE_INDEXING_CREDENTIALS`: (Optional) Google Indexing API Credentials

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Telegram Bot Setup
1. Create a bot with BotFather
2. Add bot to your channel as an administrator
3. Set webhook using the provided method in `bot.py`

## Deployment
- Push to main branch
- Vercel will automatically deploy

## Configuration
Customize `bot.py` to add more advanced indexing or processing logic

## Troubleshooting
- Ensure bot has correct channel permissions
- Check Vercel logs for deployment issues
- Verify webhook configuration

## Contributing
Contributions are welcome! Please submit a pull request.

## License
MIT License

## Contact
- Creator: Likhon Sheikh
- Telegram: @likhonsheikh
