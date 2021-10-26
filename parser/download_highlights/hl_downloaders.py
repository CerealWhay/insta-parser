import requests


def download_image(driver, xpath_to_photo, hl_name, profile_link, count):
    img_src_url = driver.find_element_by_xpath(xpath_to_photo).get_attribute("src")
    get_img = requests.get(img_src_url)
    with open(f"result/{profile_link}_media/highlights/{hl_name}_{count}.jpg", "wb") as img_file:
        img_file.write(get_img.content)


def download_video(driver, xpath_to_video, hl_name, profile_link, count):
    video_src_url = driver.find_element_by_xpath(xpath_to_video).get_attribute("src")

    get_video = requests.get(video_src_url, stream=True)
    with open(f"result/{profile_link}_media/highlights/{hl_name}_{count}.mp4", "wb") as video_file:
        for chunk in get_video.iter_content(chunk_size=1024 * 1024):
            if chunk:
                video_file.write(chunk)