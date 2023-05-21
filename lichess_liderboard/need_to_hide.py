import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get('API_TOKEN')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SEND_EMAIL = os.environ.get('SEND_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECEIVER_ADDRESS = os.environ.get('RECEIVER_ADDRESS')
