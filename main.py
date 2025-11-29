import os

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

cl = Client()
cl.login_by_sessionid(os.environ.get("SESSION_ID"))

target_username = os.environ.get("TARGET_USERNAME")
user_info = cl.user_info_by_username(target_username).dict()
user_id = cl.user_id_from_username(target_username)

print(f"PK (Primary Key): {user_info['pk']}")
print(f"USERNAME: {user_info.get('username')}")
print(f"FULL NAME: {user_info.get('full_name')}")

if user_info.get("biography"):
    print(f"BIO: {user_info.get('biography')}")

if user_info.get("public_email") is not None:
    print(f"PUBLIC EMAIL: {user_info.get('public_email')}")

if user_info.get("public_phone_number") is not None:
    print(f"PUBLIC PHONE NUMBER: {user_info.get('public_phone_number')}")

if int(user_info.get("follower_count")) > 0:
    print("FOLLOWERS:")
    for pk, follower in cl.user_followers(user_id, amount=40).items():
        if follower.full_name:
            print(f"{pk}: {follower.full_name}")
        else:
            print(f"{pk}: {follower.username}")

if int(user_info.get("following_count")) > 0:
    print("FOLLOWING:")
    for pk, following in cl.user_following(user_id, amount=40).items():
        if following.full_name:
            print(f"{pk}: {following.full_name}")
        else:
            print(f"{pk}: {following.username}")
