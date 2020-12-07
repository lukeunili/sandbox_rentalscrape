#from typing import List

#from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import sqlite3 as sql
import datetime as datetime
import locale
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

""" IMPORTANT: SQL-PATHS HAVE BEEN EDITED AND ARE NOT USABLE IN LOCAL RUN """

class Scrape:

    # define the url what will be open
    urlpage = 'https://www.sixt.at/'
    countrycode = "AT"
    print(urlpage)

    # define chromedriver to execute headless, incl. window size
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    # run Chrome webdriver from executable path of your choice
    driver = webdriver.Chrome(options=chrome_options)


    # get web page
    driver.get(urlpage)

    #time.sleep(2)

    def convertTuple(tup):
        str =  ''.join(tup)
        return str


    """ -- CREATING PICKUPTIME LIST -- """

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor1 = conn.cursor()
    accesspickuptime = ("SELECT substr(pickuptimestart,1,5) FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor1.execute(accesspickuptime)
    pickuptimestart_tuple = cursor1.fetchone()
    cursor1.close()
    """Connect to sqlite table and fetch pickuptime as tuple"""

    pickuptimestart_str = convertTuple(pickuptimestart_tuple)
    """Convert tuple into string"""

    pickuptime_time = datetime.datetime.strptime(pickuptimestart_str, "%H:%M")
    """Convert string into datetime format"""

    pickuptime0 = pickuptime_time
    pickuptime30 = pickuptime_time + datetime.timedelta(hours=0, minutes=30, seconds=0)
    pickuptime60 = pickuptime_time + datetime.timedelta(hours=1, minutes=00, seconds=0)
    #pickuptime90 = pickuptime_time + datetime.timedelta(hours=1, minutes=30, seconds=0)
    #pickuptime120 = pickuptime_time + datetime.timedelta(hours=2, minutes=00, seconds=0)
    """Add hr:mm to first pickuptime to create 2 hr window"""

    pickuptimes = []
    """Create pickuptimes list"""

    pickuptime0_str = pickuptime0.strftime("%H:%M")
    pickuptimes.append(pickuptime0_str)
    pickuptime30_str = pickuptime30.strftime("%H:%M")
    pickuptimes.append(pickuptime30_str)
    pickuptime60_str = pickuptime60.strftime("%H:%M")
    pickuptimes.append(pickuptime60_str)
    #pickuptime90_str = pickuptime90.strftime("%H:%M")
    #pickuptimes.append(pickuptime90_str)
    #pickuptime120_str = pickuptime120.strftime("%H:%M")
    #pickuptimes.append(pickuptime120_str)
    """Append all possible pickuptimes to list"""

    print("Pickuptimes:")
    print(pickuptimes)


    """ -- CREATING DROPOFFTIME LIST -- """

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor2 = conn.cursor()
    accessdropofftime = ("SELECT substr(dropofftimestart,1,5) FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor2.execute(accessdropofftime)
    dropofftimestart_tuple = cursor2.fetchone()
    cursor2.close()
    """Connect to sqlite table and fetch dropofftime as tuple"""

    dropofftimestart_str = convertTuple(dropofftimestart_tuple)
    """Convert tuple into string"""

    dropofftime_time = datetime.datetime.strptime(dropofftimestart_str, "%H:%M")
    """Convert string into datetime format"""

    dropofftime0 = dropofftime_time
    dropofftime30 = dropofftime_time + datetime.timedelta(hours=0, minutes=30, seconds=0)
    dropofftime60 = dropofftime_time + datetime.timedelta(hours=1, minutes=00, seconds=0)
    #dropofftime90 = dropofftime_time + datetime.timedelta(hours=1, minutes=30, seconds=0)
    #dropofftime120 = dropofftime_time + datetime.timedelta(hours=2, minutes=00, seconds=0)
    """Add hr:mm to first dropofftime to create 2 hr window"""

    dropofftimes = []
    """Create dropofftimes list"""

    dropofftime0_str = dropofftime0.strftime("%H:%M")
    dropofftimes.append(dropofftime0_str)
    dropofftime30_str = dropofftime30.strftime("%H:%M")
    dropofftimes.append(dropofftime30_str)
    dropofftime60_str = dropofftime60.strftime("%H:%M")
    dropofftimes.append(dropofftime60_str)
    #dropofftime90_str = dropofftime90.strftime("%H:%M")
    #dropofftimes.append(dropofftime90_str)
    #dropofftime120_str = dropofftime120.strftime("%H:%M")
    #dropofftimes.append(dropofftime120_str)
    """Append all possible dropofftimes to list"""

    print("Dropofftimes:")
    print(dropofftimes)

    """ -- DEFINING STATION -- """

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor3 = conn.cursor()
    pullstation = ("SELECT station FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor3.execute(pullstation)
    pullstation_tuple = cursor3.fetchone()
    cursor3.close()
    """Connect to sqlite table and fetch station as tuple"""

    station_str = convertTuple(pullstation_tuple)
    """Convert tuple into string"""

    print("Station:")
    print(station_str)

    """ -- DEFINING PICKUPDATE -- """

    locale.setlocale(locale.LC_ALL, 'de_DE')
    """Set local settings to use german days and months"""

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor4 = conn.cursor()
    accesspickupdate = ("SELECT pickupdate FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor4.execute(accesspickupdate)
    pickupdate_tuple = cursor4.fetchone()
    cursor4.close()
    """Connect to sqlite table and fetch pickupdate as tuple"""

    pickupdate_str = convertTuple(pickupdate_tuple)
    """Convert tuple into string"""

    pickupdate_date = datetime.datetime.strptime(pickupdate_str, "%Y-%m-%d")
    """Convert string into datetime format"""

    pickupdate_adbY = pickupdate_date.strftime("%a. %d. %b %Y")
    print("Pick-up date:")
    print(pickupdate_adbY)


    """ -- DEFINING DROPOFFDATE -- """

    locale.setlocale(locale.LC_ALL, 'de_DE')
    """Set local settings to use german days and months"""

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor5 = conn.cursor()
    accessdropoffdate = ("SELECT dropoffdate FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor5.execute(accessdropoffdate)
    dropoffdate_tuple = cursor5.fetchone()
    cursor5.close()
    """Connect to sqlite table and fetch dropoffdate as tuple"""

    dropoffdate_str = convertTuple(dropoffdate_tuple)
    """Convert tuple into string"""

    dropoffdate_date = datetime.datetime.strptime(dropoffdate_str, "%Y-%m-%d")
    """Convert string into datetime format"""

    dropoffdate_adbY = dropoffdate_date.strftime("%a. %d. %b %Y")
    print("Drop-off date:")
    print(dropoffdate_adbY)


    """ -- DEFINING SEARCHID -- """

    conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
    cursor6 = conn.cursor()
    accesssearchid = ("SELECT id FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor6.execute(accesssearchid)
    searchid_tuple = cursor6.fetchone()
    cursor6.close()
    """Connect to sqlite table and fetch searchid as tuple"""

    searchid_int = sum(searchid_tuple)
    """Convert tuple into integer"""

    print("Search ID:")
    print(searchid_int)


    """ ------------------------------------------------------------------------------------------- """

    time.sleep(3)

    """ -- Confirm the Cockie Settings of Sixt -- """
    cookie_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[5]/div/div/div[2]/div/div/div")))
    cookie_button.click()
    time.sleep(1)

    """ -- Click and enter text into rental station field -- """
    RentalStationPicker = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "pickupStation")))
    RentalStationPicker.click()
    time.sleep(1)
    RentalStationPicker.send_keys(str(station_str))
    rental_station_confirm = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'StationList__title')]")))
    rental_station_confirm.click()

    """ -- Choose and click pick up date --- """

    rental_PickUpDateButton = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='DateButton__horizontal DateButton__wrapper']/span[@class='DateButton__date']")))
    rental_PickUpDateButton.click()
    # choose pick up date 15.01.2021


    #rental_PickupDateArrow = driver.find_element_by_css_selector("div[aria-label='Next Month']")

    """ -- IF to check, if the pick up date is displayed on the website -- """

    if driver.find_element_by_css_selector("div[aria-label='Fr. 18. Dez 2020']").is_displayed():
        print('Pickup Date: Success')
    else:
        #rental_PickupDateArrow.click()
        print("failure")

    rental_PickUpDate = driver.find_element_by_css_selector("div[aria-label='" + pickupdate_adbY + "']")
    rental_PickUpDate.click()
    time.sleep(0.5)
    # choose drop off date
    rental_DropOffDate = driver.find_element_by_css_selector("div[aria-label='" + dropoffdate_adbY + "']")
    rental_DropOffDate.click()


    # choose pick up time 13:30
    rental_PickUpTimeButton = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")))
    rental_PickUpTimeButton.click()
    time.sleep(0.5)
    rental_PickUpTime = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '" + str(pickuptime30_str) +"')]")))
    driver.execute_script('arguments[0].scrollIntoView(true);', rental_PickUpTime)
    rental_PickUpTime.click()

    print(str(pickuptime30_str))

    time.sleep(0.5)

    # choose drop off time 12:00
    time.sleep(0.5)
    rental_DropOffTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__returnDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
    rental_DropOffTimeButton.click()
    time.sleep(0.5)
    rental_DropOffTime = driver.find_element_by_xpath("//*[contains(text(), '" + str(dropofftime30_str) +"')]")
    driver.execute_script('arguments[0].scrollIntoView(true);', rental_DropOffTime)
    rental_DropOffTime.click()

    print(str(dropofftime30_str))

    # confirm the times and dates
    time.sleep(1)
    rental_ConfirmButton = driver.find_element_by_xpath("//div[contains(@class, 'SearchEngine__buttonWrapper')]")
    rental_ConfirmButton.click()
    time.sleep(2)


    # scroll until the end of the website
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(2)
    # defines all possible rental offers at the specific station and certain dates
    offers = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")
    print('Number of results', len(offers))

    # create empty array to store data
    data = []
    # loop over results
    # for result in offers:

    #    car_type_element = result.find_element_by_class_name("OfferTile__descriptionTitle")
    #    car_type = car_type_element.text

    #    car_description_element = result.find_element_by_class_name("OfferTile__descriptionText")
    #    car_description = car_description_element.text

    #    car_price_element = result.find_element_by_class_name("OfferTile__offerPriceNormal")
    #    car_price = car_price_element.text

    #    mileage_element = result.find_element_by_class_name("CheckList__checkmarkTitle")
    #    mileage = mileage_element.text

    #    pickup_date_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/span")
    #    pickup_date = pickup_date_element.text

    #    pickup_time_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span[1]")
    #    pickup_time = pickup_time_element.text

    #    dropoff_date_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/span")
    #    dropoff_date = dropoff_date_element.text

    #    dropoff_time_element = result.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span[1]")
    #    dropoff_time = dropoff_time_element.text


    #    bookingclass_element = result.find_element_by_class_name("OfferTile__wrapper")
    #    bookingclass = bookingclass_element.get_attribute("class")


        # append dict to array
    #    data.append({"cartype": car_type, "cardescription": car_description, "price": car_price[1:-6],"mileage": mileage, "pickupdate" : pickup_date, "pickuptime" : pickup_time, "dropoffdate" : dropoff_date, "dropofftime" : dropoff_time, "bookingclass": bookingclass[-4:]})

    #df = pd.DataFrame(data)
    #df.to_csv('firsttry.csv')


    for SearchPickUpTimes in pickuptimes:
        driver.execute_script("window.scrollTo(0, 0);")
        rental_PickUpTimeButton = driver.find_element_by_xpath("//*[@class='SearchEngine__pickupDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
        rental_PickUpTimeButton.click()
        time.sleep(0.5)
        #rental_PickUpTimeSearch = """ "//*[contains(text(), '""" + str(SearchPickUpTime) + """')]" """
        rental_pickuptimes = driver.find_element_by_xpath("//*[contains(text(), '" + (SearchPickUpTimes) +"')]")
        rental_pickuptimes.click()
        time.sleep(1)

        # scroll until the end of the website
        #driver.execute_script(
        #    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

        #time.sleep(2)
        #offers3 = driver.find_elements_by_xpath("//*[@class='OfferList__gridItem']")

        for SearchDropOffTime in dropofftimes:
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            rental_DropOffTimeButton2 = driver.find_element_by_xpath("//*[@class='SearchEngine__returnDateTime']//*[@class='TimeButton__horizontal TimeButton__wrapper']")
            rental_DropOffTimeButton2.click()
            time.sleep(0.5)
                # rental_PickUpTimeSearch = """ "//*[contains(text(), '""" + str(SearchPickUpTime) + """')]" """
            rental_dropofftimes = driver.find_element_by_xpath("//*[contains(text(), '" + str(SearchDropOffTime) +"')]")
            rental_dropofftimes.click()
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
                        {"cartype": car_type, "cardescription": car_description, "price": car_price, "mileage": mileage,
                         "pickupdate": pickup_date, "pickuptime": pickup_time, "dropoffdate": dropoff_date,
                         "dropofftime": dropoff_time, "bookingclass": bookingclass[-4:], "searchid": searchid_int, "countrycode": countrycode})
                df = pd.DataFrame(data)

                conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
                cursor = conn.cursor()
                df.to_sql('frontend_offer', conn, if_exists='replace', index_label="id")
            print("Sucess:", SearchPickUpTimes, SearchDropOffTime)


    df = pd.DataFrame(data)
    df.sort_values(by='price', ascending=True, ignore_index=True)

    print(df)

    # write to sqlite3
    #conn = sql.connect('../db.sqlite3')
    #cursor = conn.cursor()
    #df.to_sql('frontend_offer', conn, if_exists = 'replace', index_label = "id")
    print('Finished writing to SQL database')
