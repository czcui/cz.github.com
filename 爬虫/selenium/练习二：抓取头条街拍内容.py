from urllib.parse import urlencode
import requests
import time
import os
from hashlib import md5
import re
from multiprocessing.pool import  Pool

def get_page(offset, timestamp):
    """
    params = {'aid': '24',
        'app_name': 'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'街拍',       #%E8%A1%97%E6%8B%8
        'autoload':'true',
        'count':'30',
        'en_gc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
        'timestamp':timestamp,
    }
    """
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=30&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp={}'.format(offset, timestamp)
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('return json')
            print('response.json', response.json())
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            print('title:', title)
            images = item.get('image_list')
            print('images :', image_list)
            for image in images:
                yield{
                    'image':image.get('url'),
                    'title':title,
                }

def save_image(item):
    if not os.path.exits(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        print("1111111")
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            print(file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print("Already Downloaded", file_path)
    except requests.ConnectionError:
        print("Failed to Save Image")

def main(offset):
    time.sleep(1)
    timeret = time.time()
    #只要小数点后的
    timestamp = re.search('\d+\.\d{3}', str(timeret)).group()
    timestamp = timestamp.replace('.', '')
    json = get_page(offset, timestamp)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()