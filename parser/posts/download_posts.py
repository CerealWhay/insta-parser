import logging
import os
from pathlib import Path


def get_posts(cl, username):

    logging.info(f'saving posts from {username}.')

    try:
        user = cl.user_info_by_username(username)
        user_id = user.pk
        medias = cl.user_medias(user_id)
    except Exception as ex:
        logging.error(ex)
        return

    logging.info(f'{username} have {len(medias)} posts')

    path = f'results/{username}'
    if not os.path.exists(path):
        os.mkdir(path)

    for media in medias:
        if media.media_type == 8:
            logging.info(f'  post {media.code} is an album')
            count = 0
            for resource in media.resources:
                downloader(cl, resource, username, media.code, count)
                count += 1
            logging.info(f'  album saved.')
        else:
            downloader(cl, media, username, media.code)
    logging.info(f'posts from user {username} are saved successfully.')


def downloader(cl, media, username, media_code, count=0):
    path = f"results/{username}/posts"

    if not os.path.exists(path):
        os.mkdir(path)

    p = Path(path)

    if media.media_type == 1:
        logging.info(f'    downloading photo {media_code}_{count} ...')
        cl.photo_download_by_url(
            url=media.thumbnail_url,
            filename=f'{media_code}_{count}',
            folder=p
        )
        logging.info(f'    photo {media_code}_{count} downloaded!')
    elif media.media_type == 2:
        logging.info(f'    downloading video {media_code}_{count} ...')
        cl.video_download_by_url(
            url=media.video_url,
            filename=f'{media_code}_{count}',
            folder=p
        )
        logging.info(f'    video {media_code}_{count} downloaded!')
    else:
        print(f"    {media_code}_{count} raised an error")
