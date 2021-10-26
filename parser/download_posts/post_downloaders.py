import logging

import requests


def download_image(link, profile_link, post_url, count=0):
    get_img = requests.get(link)
    with open(f"result/{profile_link}_media/posts/{post_url.split('/')[-2]}_{count}.jpg", "wb") as img_file:
        img_file.write(get_img.content)


def download_video(link, profile_link, post_url, count=0):
    get_video = requests.get(link, stream=True)
    with open(f"result/{profile_link}_media/posts/{post_url.split('/')[-2]}_{count}.mp4", "wb") as video_file:
        for chunk in get_video.iter_content(chunk_size=1024 * 1024):
            if chunk:
                video_file.write(chunk)


def download_nested_image(links, profile_link, post_url):
    count = 1
    for link in links:
        if link['node']['__typename'] == 'GraphImage':
            logging.info(f'    Downloading image {count}...')

            download_image(link['node']['display_url'], profile_link, post_url, count)
        elif link['node']['__typename'] == 'GraphVideo':
            logging.info(f'    Downloading video {count}...')

            download_video(link['node']['video_url'], profile_link, post_url, count)
        else:
            logging.error(f'    media {count} in {post_url} raised an error')
        count += 1
