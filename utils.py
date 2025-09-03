from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

locator = {
    'home': (By.XPATH, '//*[@id="app-root"]/header/div[1]/a'),
    'join_keydrop': (By.XPATH, '//*[@id="app-root"]/header/div/div[2]/a'),
    'terms_of_service': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/label[1]/div'),
    'age_confirmation': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/label[2]/div'),
    'login_keydrop': (By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div[2]/div[2]/button'),
    'username_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input'),
    'password_input': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input'),
    'login_steam': (By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]')
}

def keydrop(driver, row):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['join_keydrop'])).click()
    
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['terms_of_service'])).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['age_confirmation'])).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['login_keydrop'])).click()
    sleep(2)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['username_input'])).send_keys(row['LOGIN'])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['password_input'])).send_keys(row['PASS'])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator['login_steam'])).click()


    sleep(5)
    return "AWARD"