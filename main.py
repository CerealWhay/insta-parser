import logging

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from parser.download_highlights.download_highlights import download_highlights
from parser.download_posts.download_media import download_all_media
from parser.download_posts.post_descriptions import download_all_post_descriptions
from parser.login import login
from utils.config import PASSWORD, USERNAME, PROFILE_LINK
from utils.logger import set_logger_config

if __name__ == '__main__':
    # set logger
    set_logger_config()

    # set options
    options = Options()
    options.headless = True

    # start driver
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)

    # === STARTS PARSER ===

    # login in instagram
    login(driver, USERNAME, PASSWORD)

    # start download posts
    # download_all_media(driver, PROFILE_LINK)

    # start download highlights
    # download_highlights(driver, PROFILE_LINK)

    # get post descriptions
    download_all_post_descriptions(driver, PROFILE_LINK)

    logging.info("===== SCRIPT ENDED =====")
    # exit driver
    driver.quit()
