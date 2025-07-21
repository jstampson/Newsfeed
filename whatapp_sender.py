from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox
TO_WHATSAPP_NUMBER = "whatsapp:+491775887091"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(body: str):
    message = client.messages.create(
        body=body,
        from_=FROM_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )
    print("✅ Text message sent:", message.sid)
