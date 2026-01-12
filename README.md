# Translator_Telegram_Bot
This bot transliterates full names from Cyrillic to Latin according to the MFA Order No. 2113 (12.02.2020).

### Requirements
- Docker
- Telegram Bot Token

### Setup
Create a `.env` file in the project root with the following content:

```env
TOKEN_BOT=your_telegram_bot_token_here
```
### build Docker image and run Docker container
docker build -t telegram-bot .
docker run --env-file .env telegram-bot

#### Be careful: do not commit your `.env` file to the repository.