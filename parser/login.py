import logging
import random
import time

from selenium.webdriver import Keys

from utils.logger import divider
from .utils import close_browser


def login(driver, username, password):
    logging.info("===== SCRIPT STARTED =====")

    try:
        driver.get('https://www.instagram.com/')
        logging.info('Connected to Instagram.')

        time.sleep(random.randrange(3, 5))

        # ADD wrong data handler
        username_input = driver.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randrange(3, 5))

        password_input = driver.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(1, 2))

        password_input.send_keys(Keys.ENTER)

        logging.info(f'Successful login ({username}).')
        divider()

    except Exception as ex:
        logging.error(ex)
        close_browser(driver)

    time.sleep(random.randrange(8, 10))
