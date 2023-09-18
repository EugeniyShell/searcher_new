from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://apteka.ru/search/?q={search}')
    res_list = []
    res = driver.find_elements(By.CSS_SELECTOR,
                               '.ViewSearch .catalog-card.card-flex')
    if len(res):
        for elem in res:
            try:
                unit = {
                    'name': elem.find_element(
                        By.CSS_SELECTOR, '.catalog-card__name'
                    ).text + ' ' + ' '.join(
                        [item.text for item in
                         elem.find_elements(By.CSS_SELECTOR,
                                            '.catalog-card__vendor')]
                    ) + ' ' + ' '.join(
                        [item.text for item in
                         elem.find_elements(By.CSS_SELECTOR, '.card-param')]
                    ),
                    'price': elem.find_element(
                        By.CSS_SELECTOR, '.moneyprice__roubles'
                    ).text,
                    'link': elem.find_element(
                        By.CSS_SELECTOR, '.catalog-card__link'
                    ).get_attribute('href'),
                    'instock': elem.find_element(
                        By.CSS_SELECTOR,
                        '.card-order-section .light-button__label'
                    ),
                }
                p_add = elem.find_elements(
                    By.CSS_SELECTOR, '.moneyprice__pennies'
                )
                if len(p_add):
                    unit['price'] += p_add[0].text
                res_list.append(unit)
            except Exception as e:
                print(e)
    else:
        try:
            elem = driver.find_element(By.CSS_SELECTOR,
                                       '.ViewProductPage')
            res_list.append({
                'name': elem.find_element(
                    By.CSS_SELECTOR, '.ViewProductPage__title h1'
                ).text,
                'price': elem.find_element(
                    By.CSS_SELECTOR,
                    '.ProductOffer__price .moneyprice__roubles'
                ).text + elem.find_element(
                    By.CSS_SELECTOR,
                    '.ProductOffer__price .moneyprice__pennies'
                ).text,
                'link': f'https://apteka.ru/product/'
                        f'{elem.get_attribute("id")}/',
            })
        except Exception as e:
            print(e)
    return res_list
