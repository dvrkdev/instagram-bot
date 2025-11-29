from instagrapi import Client

from core.exceptions import LoginRequired
from core.logger import console


def login(session_id: str) -> Client:
    cl = Client()
    try:
        cl.login_by_sessionid(session_id)
        console.print("[green][+][/green] Logged in successfully!")
        return cl

    except LoginRequired:
        console.print("[red][!][/red] Login failed: SESSION_ID invalid.")
        raise
