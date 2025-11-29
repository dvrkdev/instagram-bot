from core.logger import console
from core.exceptions import ALL_EXCEPTIONS
from utils.env_loader import load_env
from services.auth_service import login
from services.user_service import get_user_info
from services.media_service import get_recent_medias, get_comments

def main():
    try:
        SESSION_ID, TARGET_USERNAME = load_env()
        cl = login(SESSION_ID)
        
        # USER INFO
        user = get_user_info(cl, TARGET_USERNAME)
        user_id = user['pk']

        # POSTS
        medias = get_recent_medias(cl, user_id)

        # COMMENTS OF FIRST MEDIA
        if medias:
            get_comments(cl, medias[0].pk, amount=10)

    except ALL_EXCEPTIONS as e:
        console.print(f'[red][!][/red] Unexpected error: {e}')

if __name__ == '__main__':
    main()