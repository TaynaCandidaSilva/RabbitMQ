import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "message": message,
    }
    requests.post(url, data=payload)

token = "<TELEGRAM_BOT_TOKEN>"
chat_id = "<TELEGRAM_CHAT_ID>"
message = "Hello, world!"

send_telegram_message(token, chat_id, message)