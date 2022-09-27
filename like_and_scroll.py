from time import sleep
from selenium.webdriver.common.by import By
import random

class like_and_scroll_home():
    """一番最初のページをいいねして、スクロールする、"""
    def __init__(self,driver):
        self.driver = driver

    def Do_Push_like(self):
        """いいね！
        """
        insta_elem_count = len(self.driver.find_elements(By.CLASS_NAME,'_ae1h'))
        insta_elem = self.driver.find_elements(By.CLASS_NAME,'_ae1h')[int(insta_elem_count/2)-1]
        insta_elem = insta_elem.find_element(By.CLASS_NAME,'_aamw')
        if len(insta_elem.find_elements(By.TAG_NAME,'div')) == 2:
            try:
                insta_elem.find_element(By.TAG_NAME,'button').click()
                print('いいね！♡')
                sleep(1 + random.random())
            except:
                pass

    def wheel(self):
        """スクロール"""
        photo_text = self.driver.find_elements(By.CLASS_NAME,'_ae1h')[-1].text
        count = 0
        while(True):
            self.driver.execute_script("window.scrollBy(0, 120)")
            if self.driver.find_elements(By.CLASS_NAME,'_ae1h')[-1].text != photo_text:break
            if count >= 15: return 'end'
            count += 1
            sleep(0.1 + random.random()*0.2)
        
class like_and_scroll_search():
    """検索した後をいいねして、スクロールする"""
    def __init__(self,driver):
        self.driver = driver

    def Do_Push_like(self):
        like_elem = self.driver.find_element(By.CLASS_NAME,'_aamw')
        if len(like_elem.find_elements(By.TAG_NAME,'div')) == 2:
            like_elem.find_element(By.TAG_NAME,'button').click()
            sleep(1 + random.random())

    def Click_first_photo(self):
        photoraw = self.driver.find_element(By.CLASS_NAME,'_ac7v')
        photoraw.find_element(By.TAG_NAME,'a').click()
        sleep(2)

    def move_next(self):
        if len(self.driver.find_elements(By.CLASS_NAME,'_aaqg')) != 0:
            move_elem = self.driver.find_element(By.CLASS_NAME,'_aaqg')
            move_elem.find_element(By.TAG_NAME,'button').click()
            sleep(1 + random.random())
        else: return'end'
# main article _aanc _aabd a .href #URL _aabdで複数


if __name__ == '__main__':
    import LoginInstagram as li
    import control
    profile = 'instagram_auto_like_mer'

    driver = li.access_to_instageam(profile)
    
    search_rezult = control.do_search(driver,'メルカリ')
    if search_rezult == 'success':
        search = like_and_scroll_search(driver)
        search.Click_first_photo()
        for _ in range(200):
            search.Do_Push_like()
            if search.move_next() == 'end':break
    """
    insta = like_and_scroll_home(driver) # インスタンス化
    for _ in range(100):
        insta.Do_Push_like()
        condition = insta.wheel()
        if condition == 'end': 
            break
    """
