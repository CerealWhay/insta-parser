import logging
import random
import time

from selenium.webdriver import Keys


def login(driver, username, password):

    try:
        driver.get('https://www.instagram.com/')
        logging.info('Selenium connected to Instagram.')

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

        logging.info(f'successful login ({username}).')

    except Exception as ex:
        logging.error(ex)
        driver.quit()

    time.sleep(random.randrange(8, 10))
