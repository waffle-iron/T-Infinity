import os
import sys

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(username='Null', password='Null', browser='chrome', database='live'):
    """"Logs user into the tesseract stock system"""
    if 'driver' not in sys.path:
        driver_in_path = False
    else:
        driver_in_path = True

    if browser is "chrome":
        driver_name = 'chromedriver.exe'
    elif browser is 'firefox':
        driver_name = 'geckodriver.exe'
    else:
        driver_name = False

    if driver_in_path and driver_name is 'chromedriver.exe':
        driver = webdriver.Chrome()
    elif driver_in_path and driver_name is 'geckodriver.exe':
        driver = webdriver.Firefox()

    if not driver_in_path:
        file_path = os.path.join(os.path.dirname(__file__) + '/bin/' + driver_name)
        if browser is 'firefox':
            driver = webdriver.Firefox(executable_path=file_path)
        elif browser is 'chrome':
            driver = webdriver.Chrome(executable_path=file_path)

    if driver:
        wait = WebDriverWait(driver, 5)

    if database is 'live':
        driver.get('https://tesseract-cloud2.co.uk/SC51/SC_Login/aspx/Login_Launch.aspx?source=wn93kn83')
    elif database is 'test':
        driver.get('https://tesseract-cloud2.co.uk/SC51/SC_Login/aspx/Login_Launch.aspx?source=wn93kn83')

    elem_username = driver.find_element_by_id('txtUserName')
    elem_username.send_keys(username)
    elem_password = driver.find_element_by_id('txtPassword')
    elem_password.send_keys(password)
    driver.find_element_by_id('btnsubmit').click()
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass
    try:
        wait.until(EC.title_contains("Wincor"))
    except TimeoutException:
        pass


login('kieranw', 'kieranw', 'firefox', 'test')
