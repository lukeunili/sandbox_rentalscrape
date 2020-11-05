# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# specify the url
urlpage = 'https://www.sixt.at/#/reservation/offerlist'
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox()

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 5s
time.sleep(5)
#click cookie button
cookie_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/div/div/div[2]/div/div/div")
cookie_button.click()
time.sleep(2)
rental_station = driver.find_element_by_xpath('//*[@id="pickupStation"]')
rental_station.click()
time.sleep(0.5)
rental_station.send_keys("Hamburg Flughafen")
time.sleep(2)
rental_station_confirm = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div')
rental_station_confirm.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(2)
offers = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")
print('Number of results', len(offers))

# create empty array to store data
data = []
# loop over results
for result in offers:
    car_type = result.text
    #link = result.find_element_by_xpath("//*[@class='OfferTile__descriptionTitle']")
    link = result.find_element_by_xpath("//*[@class='OfferTile__descriptionTitle']")
    car_price = result.text
    link = result.find_element_by_xpath("//*[@class='OfferTile__offerPriceNormal']")
    # append dict to array
    data.append({"car type": car_type, "price": car_price})

time.sleep(5)

pickup_time = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]")
pickup_time.click()

pickup_time_select = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/span/div/div/div[2]/div/div/div[28]/span")
pickup_time_select.click()

# close driver
#driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('scraperesults/firsttry.csv')

