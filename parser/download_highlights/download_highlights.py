import logging
import random
import time

from selenium.webdriver.common.by import By

from parser.download_highlights.hl_downloaders import download_image, download_video
from parser.download_highlights.xpaths import (
    xpath_to_highlights_button,
    xpath_to_pause_button,
    xpath_to_next_button,
    xpath_to_video,
    xpath_to_media_name,
    xpath_to_photo
)
from parser.utils import xpath_exists, get_to_page, create_media_folder, close_browser
from utils.logger import divider


def download_highlights(driver, profile_link):
    get_to_page(driver, profile_link)
    logging.info(f'Connected to {profile_link}')
    create_media_folder(profile_link)
    time.sleep(random.randrange(3, 5))

    if xpath_exists(driver, xpath_to_highlights_button):
        try:
            logging.info(f'Highlights founded.')

            # go to highlights
            driver.find_element(By.XPATH, xpath_to_highlights_button).click()
            time.sleep(random.randrange(4, 5))

            # stops playing video
            play_btn = driver.find_element(By.XPATH, xpath_to_pause_button)
            # play_btn.click()

            logging.info(f'===== DOWNLOAD STARTED =====')

            count = 1
            while xpath_exists(driver, xpath_to_next_button):

                # stops playing video
                if play_btn.find_element(By.TAG_NAME, "svg").get_attribute("aria-label") == 'Pause':
                    play_btn.click()

                # get hl name
                hl_name = driver.find_element_by_xpath(xpath_to_media_name).text
                logging.info(f'Highlight name is {hl_name}')

                if xpath_exists(driver, xpath_to_video):

                    logging.info('  There is one video.')
                    logging.info(f'    Downloading video...')

                    download_video(driver, xpath_to_video, hl_name, profile_link, count)

                    logging.info(f"Video downloaded successfully!")

                elif xpath_exists(driver, xpath_to_photo):

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
            divider()

        except Exception as ex:
            logging.error(ex)
            close_browser(driver)

    else:
        return
