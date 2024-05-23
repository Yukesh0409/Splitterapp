from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def setOptions(chromeOptions,location):
    prefs = {"download.default_directory" : location}
    chromeOptions.add_experimental_option("prefs",prefs)

def creating_whatsapp_group(receiver_name):
    new_chat_button = driver.find_element(By.XPATH,"//div[@title='Menu']")
    new_chat_button.click()
    time.sleep(2)
    print("Clicked new chat button")

    new_group_option = driver.find_element(By.XPATH,"//div[@aria-label='New group']")
    new_group_option.click()
    time.sleep(2)
    print("Selected new group option")

    search_field = driver.find_element(By.XPATH,"//input[@placeholder='Search name or number']")
    search_field.send_keys(receiver_name)
    time.sleep(2)
    print("Searched receiver name")

    search_field.send_keys(Keys.RETURN)
    time.sleep(2)
    print("Selected the receiver")

    next_button = driver.find_element(By.XPATH,"//div[@aria-label='Next']")
    next_button.click()
    time.sleep(2)
    print("Clicked next button")



location = r"D:\Projects\Splitter\app\Splitterapp\templates"
chromeOptions = webdriver.ChromeOptions()
setOptions(chromeOptions,location)
prefs = {"download.default_directory" : location}
chromeOptions.add_experimental_option("prefs",prefs)
url = "https://web.whatsapp.com/"
driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)
input()
print("test site")
group_name = "Testing Splitterapp"
receiver_name = "Simren"
creating_whatsapp_group(receiver_name)









