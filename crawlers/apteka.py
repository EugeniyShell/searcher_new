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
                vars = elem.find_elements(
                    By.CSS_SELECTOR, '.CardVariants__list > a'
                )
                if len(vars):
                    for v in vars:
                        v.find_elements()
                        _unit = unit
                        _unit['name'] += ' ' + v.text
                        _unit['link'] = v.get_attribute('href')
                        res_list.append(_unit)
                else:
                    res_list.append(unit)
            except Exception as e:
                print(e)
    else:
        vars = driver.find_elements(
            By.CSS_SELECTOR, '.ViewProductPage .ProductVariants .variantButton__link'
        )
        if len(vars):
            for v in vars:
                try:
                    unit = {
                        'name': v.get_attribute('aria-label'),
                        'price': v.find_element(
                            By.CSS_SELECTOR, 'meta [itemprop="price"]'
                        ).get_attribute('content'),
                        'link': v.get_attribute('href'),
                    }
                    res_list.append(unit)
                except Exception as e:
                    print(e)
    return res_list
