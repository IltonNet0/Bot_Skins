from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pickle

locator = {
    'home': (By.XPATH, '//*[@id="app-root"]/header/div[1]/a'),
    'join_keydrop': (By.XPATH, '//*[@id="app-root"]/header/div/div[2]/a'),
    'terms_of_service': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/label[1]/div'),
    'age_confirmation': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/label[2]/div'),
    'login_keydrop': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/button'),
    'username_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'),
    'password_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'),
    'login_steam': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]'),
    'close_sell': (By.XPATH, '/html/body/div[8]/div/div/div/div[2]/div/div[3]/div[2]/button[1]'),
    'award_keydrop': (By.XPATH,'/html/body/div[1]/main/div[3]/ul/li[1]/button/div/div/canvas'),
}

def save_cookies(driver, file):
    with open(file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver,file):
    with open(file, "rb") as f:
        cookies = pickle.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()


def keydrop(driver, row):

    # sleep(5)
    # save_cookies(driver, "cookies_key-drop.pkl")

    load_cookies(driver, "cookies_key-drop.pkl")

    redeem_buttom = driver.find_element(*locator['award_keydrop'])
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", redeem_buttom)

    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['close_sell'])).click()
    except:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locator['award_keydrop'])).click()



    sleep(5)


    return "AWARD"