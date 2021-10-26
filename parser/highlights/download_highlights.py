import logging
import random
import time

from selenium.webdriver.common.by import By

from parser.highlights.login import login
from parser.highlights.utils import download_image, download_video, create_media_folder, is_xpath_exists
from parser.highlights.xpaths import (
    xpath_to_highlights_button,
    xpath_to_pause_button,
    xpath_to_next_button,
    xpath_to_video,
    xpath_to_media_name,
    xpath_to_photo
)
from utils.config import ACCOUNT_USERNAME, ACCOUNT_PASSWORD


def download_highlights(driver, profile_link):
    logging.info(f'saving highlights from {profile_link}.')

    driver.get(f"https://www.instagram.com/{profile_link}")
    logging.info(f'Selenium connected to {profile_link}')
    create_media_folder(profile_link)
    time.sleep(random.randrange(3, 5))

    if is_xpath_exists(driver, xpath_to_highlights_button):
        try:
            logging.info(f'Highlights founded.')

            # go to highlights
            driver.find_element(By.XPATH, xpath_to_highlights_button).click()
            time.sleep(random.randrange(4, 5))

            # stops playing video
            play_btn = driver.find_element(By.XPATH, xpath_to_pause_button)
            # play_btn.click()

            logging.info(f'===== HIGHLIGHTS DOWNLOAD STARTED =====')

            count = 1
            while is_xpath_exists(driver, xpath_to_next_button):

                # stops playing video
                if play_btn.find_element(By.TAG_NAME, "svg").get_attribute("aria-label") == 'Pause':
                    play_btn.click()

                # get hl name
                hl_name = driver.find_element_by_xpath(xpath_to_media_name).text
                logging.info(f'Highlight name is {hl_name}')

                if is_xpath_exists(driver, xpath_to_video):

                    logging.info('  There is one video.')
                    logging.info(f'    Downloading video...')

                    download_video(driver, xpath_to_video, hl_name, profile_link, count)

                    logging.info(f"Video downloaded successfully!")

                elif is_xpath_exists(driver, xpath_to_photo):

                    logging.info('  There is one photo.')
                    logging.info(f'    Downloading photo...')

                    download_image(driver, xpath_to_photo, hl_name, profile_link, count)

                    logging.info(f"Photo downloaded successfully!")

                else:
                    logging.error(f'{count} highlight raised an error')

                count += 1

                time.sleep(random.randrange(2, 3))
                driver.find_element(By.XPATH, xpath_to_next_button).click()
                time.sleep(0.5)

            logging.info(f'Highlights from {profile_link} are saved!')

        except Exception as ex:
            logging.error(ex)
            driver.quit()

    else:
        logging.info(f'Highlights not founded.')
        return

