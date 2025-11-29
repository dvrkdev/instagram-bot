from core.exceptions import ALL_EXCEPTIONS
from core.logger import console
from services.auth_service import login
from services.media_service import get_comments, get_recent_medias
from services.user_service import get_user_info
from utils.env_loader import load_env


def main():
    try:
        SESSION_ID, TARGET_USERNAME = load_env()
        cl = login(SESSION_ID)

        # USER INFO
        user = get_user_info(cl, TARGET_USERNAME)
        user_id = user["pk"]

        # POSTS
        medias = get_recent_medias(cl, user_id)

        # COMMENTS OF FIRST MEDIA
        if medias:
            get_comments(cl, medias[0].pk, amount=10)

    except ALL_EXCEPTIONS as e:
        console.print(f"[red][!][/red] Unexpected error: {e}")


if __name__ == "__main__":
    main()
