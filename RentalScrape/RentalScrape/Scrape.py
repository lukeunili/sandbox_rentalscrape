# import libraries
#import urllib.request
#from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# specify the url
from selenium.webdriver.remote.webelement import WebElement

urlpage = 'https://www.sixt.at/'
print(urlpage)
# run Chrome webdriver from executable path of your choice
driver = webdriver.Firefox()

# driver.set_driver_size(420, 480)

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 2s
time.sleep(2)
# click cookie button
cookie_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/div/div/div[2]/div/div/div")
cookie_button.click()
time.sleep(0.5)
# click and enter text into rental station button
rental_station = driver.find_element_by_xpath('//*[@id="pickupStation"]')
rental_station.click()
time.sleep(2)
rental_station.send_keys("Hamburg Flughafen")
time.sleep(2)
rental_station_confirm = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div/div/div[3]/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div[2]')
rental_station_confirm.click()
time.sleep(1)
rental_Button = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/button')
rental_Button.click()
time.sleep(2)
# scroll until the end of the website
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(2)
# defines all possible rental offers at the specific station and certain dates
offers = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")
print('Number of results', len(offers))

# create empty array to store data
data = []
# loop over results
for result in offers:

    car_type_element = result.find_element_by_class_name("OfferTile__descriptionTitle")
    car_type = car_type_element.text

    car_price_element = result.find_element_by_class_name("OfferTile__offerPriceNormal")
    car_price = car_price_element.text

    mileage_element = result.find_element_by_class_name("CheckList__checkmarkTitle")
    mileage = mileage_element.text

    pickup_date_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/span")
    pickup_date = pickup_date_element.text

    pickup_time_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]")
    pickup_time = pickup_time_element.text

    dropoff_date_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/span")
    dropoff_date = dropoff_date_element.text

    dropoff_time_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span[1]")
    dropoff_time = dropoff_time_element.text

    # bookingclass_element = result.find_elements_by_class_name("OfferTile__wrapper")
    # bookingclass = bookingclass_element.GetClassName()
    # append dict to array
    data.append({"car type": car_type, "price per day": car_price[1:-5],"mileage": mileage, "pickupdate" : pickup_date, "pickuptime" : pickup_time, "dropoffdate" : dropoff_date, "dropofftime" : dropoff_time})


time.sleep(2)
#//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div[3]/ul/div[1]/div/span/div/div[1]/div[1]/div/span
#//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div[3]/ul/div[2]/div/span/div/div[1]/div[1]/div/span
#//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div[3]/ul/div[37]/div/span/div/div[1]/div[1]/div/span
#pickup_time = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]")
#pickup_time.click()

#pickup_time_select = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/span/div/div/div[2]/div/div/div[28]/span")
#pickup_time_select.click()

# close driver
#driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('firsttry.csv')

#driver.close()