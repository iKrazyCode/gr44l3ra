from  mydriver import MyDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from mydriver import MyDriver
import random



mydriver = MyDriver(not_window=False)
driver = mydriver.driver

link = "https://era.graalonline.com"
graal = driver.get(link)


print('debug')


