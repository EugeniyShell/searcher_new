from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://apteka.ru/search/?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.catalog-card.card-flex')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.catalog-card__name.emphasis'
                ).text + ' ' + elem.find_element(
                    By.CSS_SELECTOR,
                    '.catalog-card__vendor span'
                ).text + ' ' + ' '.join(
                    [item.text for item in elem.find_elements(
                        By.CSS_SELECTOR, '.card-param'
                    )]
                ),
                'price': elem.find_element(
                    By.CSS_SELECTOR,
                    '.moneyprice__roubles'
                ).text,
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    'a:first-child'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
