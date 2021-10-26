import logging

from parser.highlights.download_highlights import download_highlights
from parser.posts.download_posts import get_posts


def parse_profile(username, driver, cl):
    logging.info(f'trying to save {username}')
    get_posts(cl, username)
    download_highlights(driver, username)
