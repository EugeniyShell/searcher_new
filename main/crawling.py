import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import crawlers
from .defs import CHROMEDRIVER


def crawl_it(search_list):
    result = []
    for search_item in search_list:
        result += use_crawler(search_item)
    # уборка одинаковых ссылок. пока не используем.
    # temp_dict = {}
    # for item in result:
    #     if (temp_dict.get(item['link']) and temp_dict[item['link']]['price'] >
    #         item['price']) or not temp_dict.get(item['link']):
    #         temp_dict[item['link']] = item
    # result = list(temp_dict.values())
    # return result.sort(key=lambda x: x['price'])
    return result


def use_crawler(search_item):
    result = []
    options = Options()
    options.add_argument('--headless')
    service = Service(executable_path=CHROMEDRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    for fname in crawlers.__all__:
        result += res_clear(getattr(crawlers, fname)(driver, search_item))
    return result


def res_clear(reslist):
    result = []
    for res in reslist:
        res['name'] = re.sub(r'\s+', ' ', res['name']).strip()
        res['price'] = int(re.search(r'\d+', re.sub(r'(\d+) (\d+)', r'\1\2', res['price'])).group())
        result.append(res)
    return result
