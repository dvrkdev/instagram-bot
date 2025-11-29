from rich.table import Table
from core.logger import console
from core.exceptions import UserNotFound

def get_user_info(cl, username: str) -> dict | None:
    try:
        user = cl.user_info_by_username(username).dict()

        table = Table(title=f'User: {username}')
        table.add_column('Field', style='cyan')
        table.add_column('Value', style='magenta')

        for key in ['username', 'full_name', 'biography', 'follower_count', 'following_count', 'media_count']:
            table.add_row(key, str(user.get(key, '—')))

        console.print(table)
        return user
    except UserNotFound:
        console.print(f'[red][!][/red] User not fount: {username}')
        raise