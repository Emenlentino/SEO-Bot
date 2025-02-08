# src/notifications.py
from smtplib import SMTP
from email.mime.text import MIMEText
from twilio.rest import Client as TwilioClient
from telegram import Bot as TelegramBot
import logging
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD, \
                   TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, \
                   TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("notifications")

def send_email(recipient_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email

    try:
        with SMTP(EMAIL_HOST, EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            logger.info("Email sent successfully!")
    except Exception as err:
        logger.error(f"Error sending email: {err}")

def send_sms(recipient_phone, message):
    client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=recipient_phone)
        logger.info("SMS sent successfully!")
    except Exception as err:
        logger.error(f"Error sending SMS: {err}")

def send_telegram(message):
    bot = TelegramBot(token=TELEGRAM_BOT_TOKEN)
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logger.info("Telegram message sent!")
    except Exception as err:
        logger.error(f"Error sending Telegram message: {err}")
