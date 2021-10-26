import json
import logging
import random
import time

import requests
from selenium.webdriver.common.by import By

from utils.logger import divider
from .post_downloaders import download_image, download_video, download_nested_image
from .get_links_to_posts import get_links_to_posts
from parser.utils import close_browser
from ..utils import create_media_folder


def download_all_media(driver, profile_link):
    logging.info(f'Profile that need to be downloaded: {profile_link}')

    get_links_to_posts(driver, profile_link)

    logging.info(f'===== DOWNLOADING STARTED =====')

    create_media_folder(profile_link)

    with open(f'result/{profile_link}_posts.txt') as file:
        urls_list = file.readlines()

    for post_url in urls_list:
        logging.info(f'Checking post {str(post_url).rstrip()}')
        try:

            driver.get(f"{post_url}?__a=1")
            time.sleep(random.randrange(2, 4))

            driver.find_element(By.ID, 'rawdata-tab').click()
            post_a = driver.find_element(By.CLASS_NAME, 'data').text

            post_dict = json.loads(post_a)

            if post_dict['graphql']['shortcode_media']['__typename'] == 'GraphImage':
                logging.info('  There is one image.')
                logging.info(f'    Downloading image...')

                download_image(post_dict['graphql']['shortcode_media']['display_url'], profile_link, post_url)

                logging.info(f"Content from post {str(post_url).rstrip()} downloaded successfully!")

            elif post_dict['graphql']['shortcode_media']['__typename'] == 'GraphVideo':
                logging.info('  There is one video.')
                logging.info(f'    Downloading video...')

                download_video(post_dict['graphql']['shortcode_media']['video_url'], profile_link, post_url)

                logging.info(f"Content from post {str(post_url).rstrip()} downloaded successfully!")

            elif post_dict['graphql']['shortcode_media']['__typename'] == 'GraphSidecar':
                logging.info('  There is multiple media.')

                download_nested_image(
                    post_dict['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'],
                    profile_link,
                    post_url
                )

                logging.info(f"Content from post {str(post_url).rstrip()} downloaded successfully!")
            else:
                logging.error(f'{str(post_url).rstrip()} raised an error')
        except Exception as ex:
            logging.error(ex)
            return

    logging.info(f'Posts from {profile_link} are saved!')
    divider()
