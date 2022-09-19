from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import random
class instagram_startup():
    def __init__(self):
        """seleniumの起動設定を行い、起動する。
        """

        user = getpass.getuser()
        user_data_dir_profile = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=" + user_data_dir_profile + 'instagram_auto_like')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        self.driver.get('https://www.instagram.com/')
        sleep(3)

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
            self.driver.execute_script("window.scrollBy(0, 150)")
            if self.driver.find_elements(By.CLASS_NAME,'_ae1h')[-1].text != photo_text:
                break
            sleep(random.random()*0.2)
        
        


if __name__ == '__main__':
    insta = instagram_startup() # インスタンス化
    
    for i in range(1000):
        insta.Do_Push_like()
        insta.wheel()
        