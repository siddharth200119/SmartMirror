import os
import subprocess
from selenium import webdriver
import time

os.chdir('..\\mirror_UI\\frontend\\')
subprocess.Popen('npm start', shell=True)

time.sleep(5)

driver = webdriver.Firefox()
driver.get('http://localhost:3000/')
driver.fullscreen_window()