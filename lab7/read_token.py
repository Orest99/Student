import os
import telebot
from dotenv import load_dotenv
load_dotenv()
def get_token():
    token = os.environ['Token']
    return token
