import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.keys import Keys


options = uc.ChromeOptions()

driver = uc.Chrome(options = options, version_main=138)


driver.get('https://key-drop.com/pt/daily-case')


