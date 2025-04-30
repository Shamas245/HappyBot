import os
from dotenv import load_dotenv


load_dotenv()


def load_gemini():
    gemini_key = os.environ.get('GEMINI_KEY')
    return gemini_key
