import logging
import os

from instagrapi import Client

from loader import set_selenium, set_instagrapi
from parser.profile_saver import parse_profile
from utils.config import PROFILES, ACCOUNT_USERNAME, ACCOUNT_PASSWORD
from utils.logger import set_logger_config

if __name__ == '__main__':
    # stup logger
    set_logger_config()

    logging.info('=== SCRIPT STARTS === insta-parser_v2 by CerealWhay ===')

    # make result directory
    if not os.path.exists("results"):
        os.mkdir('results')

    driver = set_selenium()
    cl = set_instagrapi()

    for profile in PROFILES:
        parse_profile(profile, driver, cl)

    logging.info(f'=== SCRIPT ENDED === thanks for using, from CW w/ love <3 ===')
    cl.logout()
    driver.quit()
