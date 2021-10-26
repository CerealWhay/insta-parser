import logging

from instagrapi import Client
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from parser.highlights.login import login
from utils.config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD


def set_selenium():

    # set options
    options = Options()
    # options.headless = True

    # start driver
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)

    login(driver, ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

    return driver


def set_instagrapi():
    # setup client
    cl = Client(request_timeout=3)
    cl.load_settings('settings_dump.json')

    # login in account
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    logging.info(f'logged in instagrAPI as {ACCOUNT_USERNAME}')

    return cl
