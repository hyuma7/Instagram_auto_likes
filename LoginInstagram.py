from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import getpass

profile = 'instagram_auto_like'

def access_to_instageam(profile):
    """seleniumの起動設定を行い、起動する。
    
    return:
        driver(web_element): インスタのドライバ
    """
    user = getpass.getuser()
    user_data_dir_profile = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data"
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=" + user_data_dir_profile + 'instagram_auto_like')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get('https://www.instagram.com/')
    sleep(3)
    return driver