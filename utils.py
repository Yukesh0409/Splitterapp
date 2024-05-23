from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

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

    search_field = driver.find_element(By.XPATH,"//div[@title='Group subject (optional)']")
    search_field.send_keys("testing_spliterapp")
    time.sleep(2)
    
    search_field.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    print("group created")

    time.sleep(5)

    print("Starting message transfer")

    input("click to start transfer")

    time.sleep(10)

def get_file_paths(directory,path_list):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)   
            path_list.append(file_path)
            print(file_path)
    return path_list


def file_transfer(file_path):
    print("hehe")
    attachment_button = driver.find_element(By.XPATH,"//div[@title='Attach']")
    attachment_button.click()
    time.sleep(3)
    document_option = driver.find_element(By.XPATH,'//input[@accept="*"]')
    document_option.send_keys(file_path)
    time.sleep(2)
    send_button = driver.find_element(By.XPATH,"//div[@aria-label='Send']")
    # send_button = driver.find_element(By.XPATH,"//span[data-icon='send']")
    send_button.click()
    time.sleep(2)

def logout():
    time.sleep(10)
    driver.quit()
    sys.exit()


def start():
    # location = r"D:\Projects\Splitter\app\Splitterapp\templates"
    # chromeOptions = webdriver.ChromeOptions()
    # setOptions(chromeOptions,location)
    # prefs = {"download.default_directory" : location}
    # chromeOptions.add_experimental_option("prefs",prefs)
    url = "https://web.whatsapp.com/"
    driver.get(url)
    input("Enter to continue")
    creating_whatsapp_group("Simren")
    path_list = []
    path_list = get_file_paths(r"D:\Projects\Splitter\app\Splitterapp\Testing\parts", path_list)
    for i in path_list:
        file_transfer(i)
        time.sleep(5)
    time.sleep(5)


driver = webdriver.Chrome()
start()








