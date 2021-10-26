import logging
import math
import random
import time

from selenium.webdriver.common.by import By

from parser.utils import get_to_page, write_list_to_file
from utils.logger import divider


def get_posts_count(driver):
    posts_count = int(driver.find_element(
        By.XPATH,
        "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
    ).text)
    logging.info(f'There is {posts_count} posts.')

    return posts_count


def get_links_to_posts(driver, profile_link):
    get_to_page(driver, profile_link)
    logging.info(f'Connected to {profile_link}')

    time.sleep(random.randrange(3, 5))

    loops_count = math.ceil(get_posts_count(driver) / 12)

    posts_links = []
    logging.info(f'Finding all links to posts. This may take some time...')
    for i in range(0, loops_count):
        # find links on dynamic page
        all_links_on_iteration = driver.find_elements(By.TAG_NAME, 'a')
        post_links_on_iteration = [
            item.get_attribute('href') for item in all_links_on_iteration if "/p/" in item.get_attribute('href')
        ]

        # append links to all_post_links
        for link in post_links_on_iteration:
            posts_links.append(link)

        # scroll to end of page to load old posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(random.randrange(2, 4))

    # delete repeating links
    posts_links = set(posts_links)
    posts_links = list(posts_links)

    # write links to file
    write_list_to_file(f'result/{profile_link}_posts', 'w', posts_links)
    logging.info(f'{len(posts_links)} links to posts saved to file {profile_link}_posts.txt.')
    divider()
