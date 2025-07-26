from twilio.rest import Client
from dotenv import load_dotenv
import os

# Lade .env aus dem Projektverzeichnis
load_dotenv(override=True)

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

FROM_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox
TO_WHATSAPP_NUMBER = "whatsapp:+491775887091"


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(body: str, media_url: str = None):
    message = client.messages.create(
        body=body,
        from_=FROM_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER,
        media_url=[media_url] if media_url else None 
        )
    print("✅ message sent:", message.sid)
