from pandas import DataFrame
from selenium import webdriver
import time
import pandas as pd


# specify the url
urlpage = 'https://www.sixt.at/'
print(urlpage)
# run Chrome webdriver from executable path of your choice
driver = webdriver.Firefox()

#driver.set_window_size(800, 2000)
time.sleep(2)
#size = driver.get_window_size()

# get web page
driver.get(urlpage)
# execute script to scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 2s
time.sleep(2)
# click cookie button
cookie_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/div/div/div[2]/div/div/div")
cookie_button.click()
time.sleep(1)
# click and enter text into rental station button
# Mobilerental_stationPicker = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/span')
RentalStationPicker = driver.find_element_by_id("pickupStation")
RentalStationPicker.click()
time.sleep(1)
#rental_station = driver.find_element_by_xpath('//*[@id="pageSlideWrapper"]/div/div/div[1]/div[2]/div/input')
#rental_station.click()
#time.sleep(2)
RentalStationPicker.send_keys("Muenchen Flughafen")
time.sleep(2)
rental_station_confirm = driver.find_element_by_xpath("//div[contains(@class, 'StationList__title')]")

rental_station_confirm.click()
time.sleep(1)
# click pick up date
rental_PickUpDateButton = driver.find_element_by_xpath("//div[@class='DateButton__horizontal DateButton__wrapper']/span[@class='DateButton__date']")
rental_PickUpDateButton.click()

# choose pick up date 15.01.2021
time.sleep(2)

#rental_PickupDateArrow = driver.find_element_by_css_selector("div[aria-label='Next Month']")

# loop to check, if the pick up date is displayed on the website
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
rental_PickUpTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
rental_PickUpTimeButton.click()
time.sleep(0.5)
rental_PickUpTime = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[3]/div/span/div/div/div[2]/div/div/div[29]")
rental_PickUpTime.click()

time.sleep(0.5)

# choose drop off time 12:00
rental_DropOffTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__returnDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
rental_DropOffTimeButton.click()
time.sleep(0.5)
rental_DropOffTime = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[3]/div/span/div/div/div[2]/div/div/div[25]")
rental_DropOffTime.click()

# confirm the times and dates
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

df = pd.DataFrame(data)
df.to_csv('firsttry.csv')


time.sleep(2)

# choose pick up time 14:30
rental_PickUpTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
rental_PickUpTimeButton.click()
time.sleep(0.5)
rental_PickUpTime = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/span/div/div/div[2]/div/div/div[30]")
rental_PickUpTime.click()

time.sleep(0.5)

# scroll until the end of the website
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(1)

# defines all possible rental offers at the specific station and certain dates
offers2 = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")
print('Number of results', len(offers2))

for result in offers2:

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

    data.append({"car type": car_type, "price per day": car_price[1:-5], "mileage": mileage, "pickupdate": pickup_date, "pickuptime": pickup_time, "dropoffdate": dropoff_date, "dropofftime": dropoff_time})

df = pd.DataFrame(data)
df.to_csv('firsttry.csv', mode='a', header=False)


print(df)

# write to csv
df.to_csv('firsttry.csv')

print('Finish!')

#driver.close()