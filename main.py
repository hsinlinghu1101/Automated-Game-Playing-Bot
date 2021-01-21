from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")
list_items = []
items = driver.find_elements_by_css_selector("#store div b")

for item in items:
    list_items.append(item.text.split(' '))

money = driver.find_element_by_css_selector("#money")


def purchase():
    available_list = []
    for item in list_items:
        if item[0] != '':
            item_price = int(item[len(item) - 1].replace(",", ''))
            money_num = money.text
            if item_price < int(money_num.replace(",", '')):
                available_list.append(item)
    target_item = available_list[-1]
    driver.find_element_by_css_selector(f"#buy{target_item[0]}").click()


timeout = time.time() + 5
five_mins = time.time() + 5*60

while True:
    cookie.click()
    if time.time() > timeout:
        purchase()
        timeout = time.time() + 5
    if time.time() > five_mins:
        cookie_secs = driver.find_element_by_css_selector("#cps")
        print(cookie_secs.text)
        break


driver.quit()
