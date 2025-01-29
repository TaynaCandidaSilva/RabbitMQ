import requests

def send_telegram_message(message: str) -> None:
    token = "<TELEGRAM_BOT_TOKEN>"
    chat_id = "<TELEGRAM_CHAT_ID>"


    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "message": message,
    }
    requests.post(url, data=payload)