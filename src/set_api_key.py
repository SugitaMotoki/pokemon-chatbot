import os
from config import OPENAI_API_KEY

def set_api_key():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY