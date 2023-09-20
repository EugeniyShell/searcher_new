import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service

import crawlers
# from .defs import CHROMEDRIVER, MSEDGEDRIVER, GECKODRIVER
from .defs import CHROMEDRIVER


def crawl_it(search_list):
    result = []
    for search_item in search_list:
        result += use_crawler(search_item)
    temp_dict = {}
    for item in result:
        temp_dict[item['link']] = item
    result = list(temp_dict.values())
    result.sort(key=lambda x: x['price_num'])
    return result


def use_crawler(search_item):
    result = []
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    service = Service(executable_path=CHROMEDRIVER)
    # service = Service(executable_path=MSEDGEDRIVER)
    # service = Service(executable_path=GECKODRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    for fname in crawlers.__all__:
        result += res_clear(getattr(crawlers, fname)(driver, search_item))
    driver.quit()
    return result


def res_clear(reslist):
    result = []
    for res in reslist:
        res['name'] = re.sub(r'\s+', ' ', res['name']).strip()
        res['price'] = re.sub(r'(\d+) (\d+)', r'\1\2', res['price'])
        res['price_num'] = float(res['price'])
        result.append(res)
    return result
