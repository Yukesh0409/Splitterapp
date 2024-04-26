from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def setOptions(chromeOptions,location):
    prefs = {"download.default_directory" : location}
    chromeOptions.add_experimental_option("prefs",prefs)

location = r"D:\Projects\Splitter\app\Splitterapp\templates"
chromeOptions = webdriver.ChromeOptions()
setOptions(chromeOptions,location)
prefs = {"download.default_directory" : location}
chromeOptions.add_experimental_option("prefs",prefs)
url = "https://web.whatsapp.com/"
driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)
input()


def setOptions(chromeOptions,location):
    prefs = {"download.default_directory" : location}
    chromeOptions.add_experimental_option("prefs",prefs)



