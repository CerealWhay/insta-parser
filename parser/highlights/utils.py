import os

import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def download_image(driver, xpath_to_photo, hl_name, profile_link, count):
    img_src_url = driver.find_element_by_xpath(xpath_to_photo).get_attribute("src")
    get_img = requests.get(img_src_url)
    with open(f"results/{profile_link}/highlights/{hl_name}_{count}.jpg", "wb") as img_file:
        img_file.write(get_img.content)


def download_video(driver, xpath_to_video, hl_name, profile_link, count):
    video_src_url = driver.find_element_by_xpath(xpath_to_video).get_attribute("src")

    get_video = requests.get(video_src_url, stream=True)
    with open(f"results/{profile_link}/highlights/{hl_name}_{count}.mp4", "wb") as video_file:
        for chunk in get_video.iter_content(chunk_size=1024 * 1024):
            if chunk:
                video_file.write(chunk)


def create_media_folder(profile_link):
    if not os.path.exists(f"results/{profile_link}"):
        os.mkdir(f"results/{profile_link}")

    if not os.path.exists(f"results/{profile_link}/highlights"):
        os.mkdir(f"results/{profile_link}/highlights")


# check element exist by XPATH
def is_xpath_exists(driver, url):
    try:
        driver.find_element(By.XPATH, url)
        exist = True
    except NoSuchElementException:
        exist = False
    return exist
