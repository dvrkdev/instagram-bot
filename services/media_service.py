from rich.table import Table

from core.exceptions import MediaNotFound
from core.logger import console


def get_recent_medias(cl, user_id: int, amount: int = 5):
    medias = cl.user_medias(user_id, amount=amount)

    if not medias:
        console.print("[yellow][!][/yellow] No media found or profile is private.")
        return []

    table = Table(title="Recent Posts")
    table.add_column("PK", style="green")
    table.add_column("Caption")
    table.add_column("Likes", justify="right")
    table.add_column("Comments", justify="right")

    for m in medias:
        table.add_row(
            str(m.pk),
            (m.caption_text[:40] + "...") if m.caption_text else "-",
            str(m.like_count),
            str(m.comment_count),
        )

    console.print(table)
    return medias


def get_comments(cl, media_pk: int, amount: int = 20):
    try:
        comments = cl.media_comments(media_pk, amount=amount)

        console.print(f"Comments for media {media_pk}:")
        for c in comments:
            console.print(f"[cyan]{c.user.username}[/cyan]: {c.text}")

        return comments
    except MediaNotFound:
        console.print("[red][!][/red] Media not found.")
        raise
