import re

from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://366.ru/search/?text={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.js-product-item')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.listing_product__title'
                ).text + ' ' + elem.find_element(
                    By.CSS_SELECTOR,
                    '.listing_product__manufacturer :first-child'
                ).text,
                'price': re.sub(r'\D+', '', elem.find_element(
                    By.CSS_SELECTOR,
                    '.listing_product__price span'
                ).text),
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.listing_product__title'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
