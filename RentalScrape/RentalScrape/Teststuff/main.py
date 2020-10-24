from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/users/johannes/chromedriver')
driver.get('https://www.sixt.at/')

Cockie = "//*[@id='t3CookieCta']/div/div"
PickupStation = "//*[@id='pickupStation']"
PickupStationChoice = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[3]/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div"
PickupDate = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/span"
PickupTime = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]"
DropOffDate = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span"
DropOffTime = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/span[1]"
Button = "//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/button"


CockieElement = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(Cockie))
CockieElement.click()


PickupStationElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PickupStation))
PickupStationElement.click()
PickupStationElement.send_keys('Frankfurt Flughafen')

PickupStationChoiceElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(PickupStationChoice))
PickupStationChoiceElement.click()


ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(Button))
ButtonElement.click()


sleep(5)

driver.quit()