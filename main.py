from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

cl = Client()
cl.login_by_sessionid(os.environ.get('SESSION_ID'))

user_info = cl.user_info_by_username('').dict()
user_id = cl.user_id_from_username('')
print(f'PK (Primary Key): {user_info['pk']}')
print(f'USERNAME: {user_info.get('username')}')
print(f'FULL NAME: {user_info.get('full_name')}')
if user_info.get('biography'): print(f'BIO: {user_info.get('biography')}')
if user_info.get('public_email') is not None: print(f'PUBLIC EMAIL: {user_info.get('public_email')}')
if user_info.get('public_phone_number') is not None: print(f'PUBLIC PHONE NUMBER: {user_info.get('public_phone_number')}')
if int(user_info.get('follower_count')) > 0:
    for pk, follower in cl.user_followers(user_id, amount=40).items():
        print(f'{follower.full_name}')
                                                                                   