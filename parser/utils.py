import logging
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def get_to_page(driver, link):
    driver.get(f"https://www.instagram.com/{link}")


def create_media_folder(profile_link):
    if os.path.exists(f"result/{profile_link}_media"):
        logging.info(f"Folder result/{profile_link}_media already exist.")
    else:
        os.mkdir(f"result/{profile_link}_media")
        os.mkdir(f"result/{profile_link}_media/posts")
        os.mkdir(f"result/{profile_link}_media/highlights")
        logging.info(f"created folder for media ({profile_link}_media).")


def write_list_to_file(filepath, filemode, data_list):
    logging.info(f'Saving data to file...')
    with open(f'{filepath}.txt', f'{filemode}') as file:
        for data in data_list:
            file.write(data + "\n")


def close_browser(driver):
    driver.quit()


# check element exist by XPATH
def xpath_exists(driver, url):
    try:
        driver.find_element(By.XPATH, url)
        exist = True
    except NoSuchElementException:
        exist = False
    return exist
