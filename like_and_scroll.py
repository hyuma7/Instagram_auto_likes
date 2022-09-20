from time import sleep
from selenium.webdriver.common.by import By
import random

class like_and_scroll():
    """いいねして、スクロールする"""
    def __init__(self,driver):
        """seleniumの起動設定を行い、起動する。
        """
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

        while(True):
            self.driver.execute_script("window.scrollBy(0, 120)")
            if self.driver.find_elements(By.CLASS_NAME,'_ae1h')[-1].text != photo_text:
                break
            sleep(random.random()*0.2)
        
        

if __name__ == '__main__':
    import LoginInstagram as li
    driver = li.access_to_instageam()
    insta = like_and_scroll(driver) # インスタンス化
    for i in range(100):
        insta.Do_Push_like()
        insta.wheel()