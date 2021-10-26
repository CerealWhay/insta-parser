import json
import logging
import random
import re
import time

import requests
from selenium.webdriver.common.by import By

from parser.download_posts.get_links_to_posts import get_links_to_posts
from parser.utils import close_browser, write_list_to_file, get_to_page
from utils.logger import divider


def download_all_post_descriptions(driver, profile_link):
    logging.info(f'Profile that need to get profile references: {profile_link}')

    # get_links_to_posts(driver, profile_link)

    with open(f'result/{profile_link}_posts.txt') as file:
        urls_list = file.readlines()

    links = []
    for post_url in urls_list:
        logging.info(f'Checking post {str(post_url).rstrip()}')
        try:

            driver.get(f"{post_url}?__a=1")
            time.sleep(random.randrange(1, 2))

            driver.find_element(By.ID, 'rawdata-tab').click()
            post_a = driver.find_element(By.CLASS_NAME, 'data').text

            post_dict = json.loads(post_a)

            # finding description
            if post_dict['graphql']['shortcode_media']['edge_media_to_caption']['edges']:

                description = post_dict['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']

                find_link_in_description = re.search(r'(@\S+)', description)

                # finding profile_link
                if find_link_in_description:
                    link_to_other_profile = find_link_in_description.group(0)
                    logging.info(f'  There is link to profile {link_to_other_profile}.')

                    # append link to links
                    links.append(link_to_other_profile[1:])

                else:
                    logging.info(f'  There is no link to profile.')

            else:
                logging.info(f'  There is no description.')

        except Exception as ex:
            logging.error(ex)
            return

    # delete repeating links
    links = set(links)
    links = list(links)

    # write links to file
    write_list_to_file(f'result/{profile_link}_links', 'w', links)
    logging.info(f'Links to profiles saved to file {profile_link}_links.txt.')
    divider()
