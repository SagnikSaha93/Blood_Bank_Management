from selenium import webdriver
#For installing Chrome Webdriver Manager Automatically in any system and run the scripts
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #https://pypi.org/project/webdriver-manager/

#driver = webdriver.Chrome() #It's needed when you manually install chromedriver.exe

#Open the Link
driver.get("https://sagniksaha93.github.io/Sagnik_Saha/")

#Maximize the Window
maxi_window = driver.maximize_window()

#Get the title of the WebPage
title = driver.title
print (title)

#Close the Current Browser
driver.close()