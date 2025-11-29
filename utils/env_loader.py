import os
from dotenv import load_dotenv
from core.logger import console

def load_env():
    load_dotenv()
    SESSION_ID = os.environ.get('SESSION_ID')
    TARGET_USERNAME = os.environ.get('TARGET_USERNAME')

    if not SESSION_ID:
        console.print('[red][!][/red] SESSION_ID is missing in .env')
        raise SystemExit
    
    return SESSION_ID, TARGET_USERNAME