from time import sleep
from selenium.webdriver.common.by import By

def do_search(driver,keyword):
    driver.get(f'https://www.instagram.com/explore/tags/{keyword}/')

    if len(driver.find_elements(By.TAG_NAME,'h2')) == 1:
        print('NotGoodWord')
        return 'NotGoodWord'
    sleep(5)
    return 'success'