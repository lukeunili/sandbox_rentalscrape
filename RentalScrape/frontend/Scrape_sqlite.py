#from typing import List

#from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import sqlite3 as sql

#gettingvalues = sql.connect('../db.sqlite3')
#gettingvaluescursor = gettingvalues.cursor()
#pickupstationsearch = gettingvaluescursor.execute("select 'Station' from 'frontend_searchinput' order by id desc limit 1")

#print(pickupstationsearch)


# specify the url
urlpage = 'https://www.sixt.at/'
print(urlpage)

# define chromedriver to execute headless, incl. window size
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

# run Chrome webdriver from executable path of your choice
driver = webdriver.Chrome(options=chrome_options)

#time.sleep(2)

SearchPickUpTime = ['14:00', '14:30', '15:00']
SearchDropOffTime = ['8:00', '8:30', '9:00', '9:30']

# get web page
driver.get(urlpage)
time.sleep(5)
# click cookie button
cookie_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/div/div/div[2]/div/div/div")
cookie_button.click()
time.sleep(1)
# click and enter text into rental station button
RentalStationPicker = driver.find_element_by_id("pickupStation")
RentalStationPicker.click()
time.sleep(1)
RentalStationPicker.send_keys("Muenchen Flughafen")
time.sleep(4)
rental_station_confirm = driver.find_element_by_xpath("//div[contains(@class, 'StationList__title')]")
rental_station_confirm.click()
time.sleep(1)
# click pick up date
rental_PickUpDateButton = driver.find_element_by_xpath("//div[@class='DateButton__horizontal DateButton__wrapper']/span[@class='DateButton__date']")
rental_PickUpDateButton.click()
# choose pick up date 15.01.2021
time.sleep(2)

#rental_PickupDateArrow = driver.find_element_by_css_selector("div[aria-label='Next Month']")

# IF to check, if the pick up date is displayed on the website
if driver.find_element_by_css_selector("div[aria-label='Fr. 18. Dez 2020']").is_displayed():
    print('Pickup Date: Success')
else:
    #rental_PickupDateArrow.click()
    print("failure")

rental_PickUpDate = driver.find_element_by_css_selector("div[aria-label='Fr. 18. Dez 2020']")
rental_PickUpDate.click()
time.sleep(0.5)
# choose drop off date
rental_DropOffDate = driver.find_element_by_css_selector("div[aria-label='Mo. 21. Dez 2020']")
rental_DropOffDate.click()


# choose pick up time 13:30
time.sleep(0.5)
rental_PickUpTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
rental_PickUpTimeButton.click()
time.sleep(0.5)
rental_PickUpTime = driver.find_element_by_xpath("//*[contains(text(), '13:30')]")
rental_PickUpTime.click()

time.sleep(0.5)

# choose drop off time 12:00
time.sleep(0.5)
rental_DropOffTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__returnDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
rental_DropOffTimeButton.click()
time.sleep(0.5)
rental_DropOffTime = driver.find_element_by_xpath("//*[contains(text(), '9:00')]")
rental_DropOffTime.click()

# confirm the times and dates
time.sleep(1)
rental_ConfirmButton = driver.find_element_by_xpath("//div[contains(@class, 'SearchEngine__buttonWrapper')]")
rental_ConfirmButton.click()
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

    car_description_element = result.find_element_by_class_name("OfferTile__descriptionText")
    car_description = car_description_element.text

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


    bookingclass_element = result.find_element_by_class_name("OfferTile__wrapper")
    bookingclass = bookingclass_element.get_attribute("class")


    # append dict to array
    data.append({"cartype": car_type, "cardescription": car_description, "price": car_price[1:-6],"mileage": mileage, "pickupdate" : pickup_date, "pickuptime" : pickup_time, "dropoffdate" : dropoff_date, "dropofftime" : dropoff_time, "bookingclass": bookingclass[-4:]})

df = pd.DataFrame(data)
#df.to_csv('firsttry.csv')


for SearchPickUpTime1 in SearchPickUpTime:
    driver.execute_script("window.scrollTo(0, 0);")
    rental_PickUpTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
    rental_PickUpTimeButton.click()
    time.sleep(0.5)
    #rental_PickUpTimeSearch = """ "//*[contains(text(), '""" + str(SearchPickUpTime) + """')]" """
    rental_PickUpTime1 = driver.find_element_by_xpath("//*[contains(text(), '" + (SearchPickUpTime1) +"')]")
    rental_PickUpTime1.click()
    time.sleep(1)

    # scroll until the end of the website
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    time.sleep(2)
    offers3 = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")

    for SearchDropOffTime1 in SearchDropOffTime:
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        rental_DropOffTimeButton2 = driver.find_element_by_xpath("//*[@class='SearchEngine__returnDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
        rental_DropOffTimeButton2.click()
        time.sleep(0.5)
            # rental_PickUpTimeSearch = """ "//*[contains(text(), '""" + str(SearchPickUpTime) + """')]" """
        rental_DropoffTime2 = driver.find_element_by_xpath("//*[contains(text(), '" + str(SearchDropOffTime1) +"')]")
        print(SearchDropOffTime)
        rental_DropoffTime2.click()



        time.sleep(1)

        # scroll until the end of the website
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

        time.sleep(1)
        offers4 = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")
        for result in offers4:
            car_type_element = result.find_element_by_class_name("OfferTile__descriptionTitle")
            car_type = car_type_element.text

            car_description_element = result.find_element_by_class_name("OfferTile__descriptionText")
            car_description = car_description_element.text

            car_price_element = result.find_element_by_class_name("OfferTile__offerPriceNormal")
            car_price = car_price_element.text

            mileage_element = result.find_element_by_class_name("CheckList__checkmarkTitle")
            mileage = mileage_element.text

            pickup_date_element = result.find_element_by_xpath(
                    "/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/span")
            pickup_date = pickup_date_element.text

            pickup_time_element = result.find_element_by_xpath(
                    "/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]")
            pickup_time = pickup_time_element.text

            dropoff_date_element = result.find_element_by_xpath(
                    "/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/span")
            dropoff_date = dropoff_date_element.text

            dropoff_time_element = result.find_element_by_xpath(
                    "/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span[1]")
            dropoff_time = dropoff_time_element.text

            bookingclass_element = result.find_element_by_class_name("OfferTile__wrapper")
            bookingclass = bookingclass_element.get_attribute("class")

            data.append(
                    {"cartype": car_type, "cardescription": car_description, "price": car_price[1:-6], "mileage": mileage,
                     "pickupdate": pickup_date, "pickuptime": pickup_time, "dropoffdate": dropoff_date,
                     "dropofftime": dropoff_time, "bookingclass": bookingclass[-4:]})
            df = pd.DataFrame(data)
        print("Sucess:", SearchPickUpTime1, SearchDropOffTime1)


df = pd.DataFrame(data)
df.sort_values(by='price', ascending=True, ignore_index=True)

print(df)

# write to sqlite3
conn = sql.connect('../db.sqlite3')
cursor = conn.cursor()
df.to_sql('frontend_offer', conn, if_exists = 'replace', index_label = "id")
print('Finished writing to SQL database')
