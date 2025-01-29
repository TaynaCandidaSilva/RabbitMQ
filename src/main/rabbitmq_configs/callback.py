import json
from src.drives.telegram_sender import send_telegram_message

def rabittmq_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    formatted_msg = json.loads(msg)
    telegram_message = formatted_msg["msg"]

    send_telegram_message(telegram_message)