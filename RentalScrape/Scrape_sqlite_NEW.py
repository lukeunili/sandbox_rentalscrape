import time
import pandas as pd
import sqlite3 as sql
import datetime as datetime
import locale
import urllib
import requests


""" IMPORTANT: SQL-PATHS HAVE BEEN EDITED AND ARE NOT USABLE IN LOCAL RUN """

class Scrape:


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
    pickuptime90 = pickuptime_time + datetime.timedelta(hours=1, minutes=30, seconds=0)
    pickuptime120 = pickuptime_time + datetime.timedelta(hours=2, minutes=00, seconds=0)
    """Add hr:mm to first pickuptime to create 2 hr window"""

    pickuptimes = []
    """Create pickuptimes list"""

    pickuptime0_str = pickuptime0.strftime("%H:%M:%S")
    pickuptimes.append(pickuptime0_str)
    pickuptime30_str = pickuptime30.strftime("%H:%M:%S")
    pickuptimes.append(pickuptime30_str)
    pickuptime60_str = pickuptime60.strftime("%H:%M:%S")
    pickuptimes.append(pickuptime60_str)
    pickuptime90_str = pickuptime90.strftime("%H:%M:%S")
    pickuptimes.append(pickuptime90_str)
    pickuptime120_str = pickuptime120.strftime("%H:%M:%S")
    pickuptimes.append(pickuptime120_str)
    """Append all possible pickuptimes to list"""

    print("Pickuptimes:")
    print(pickuptimes)


    """ -- CREATING dropoffTIME LIST -- """

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
    dropofftime90 = dropofftime_time + datetime.timedelta(hours=1, minutes=30, seconds=0)
    dropofftime120 = dropofftime_time + datetime.timedelta(hours=2, minutes=00, seconds=0)
    """Add hr:mm to first dropofftime to create 2 hr window"""

    dropofftimes = []
    """Create dropofftimes list"""

    dropofftime0_str = dropofftime0.strftime("%H:%M:%S")
    dropofftimes.append(dropofftime0_str)
    dropofftime30_str = dropofftime30.strftime("%H:%M:%S")
    dropofftimes.append(dropofftime30_str)
    dropofftime60_str = dropofftime60.strftime("%H:%M:%S")
    dropofftimes.append(dropofftime60_str)
    dropofftime90_str = dropofftime90.strftime("%H:%M:%S")
    dropofftimes.append(dropofftime90_str)
    dropofftime120_str = dropofftime120.strftime("%H:%M:%S")
    dropofftimes.append(dropofftime120_str)
    """Append all possible dropofftimes to list"""

    print("dropofftimes:")
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

    pickupdate_adbY = pickupdate_date.strftime("%Y-%m-%d")
    print("Pick-up date:")
    print(pickupdate_adbY)


    """ -- DEFINING dropoffDATE -- """

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

    dropoffdate_adbY = dropoffdate_date.strftime("%Y-%m-%d")

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




    """ -- Rental station -- """

    pickupaddress = str(station_str)
    n = 1
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(pickupaddress) + '?format=json'

    location_response = requests.get(url).json()
    lat = location_response[0]["lat"]
    lon = location_response[0]["lon"]

    station_response = requests.get(
        "https://web-api.orange.sixt.com/v1/locations/geo?latitude=" + lat + "&longitude=" + lon)
    content = station_response.json()

    print()

    print("Your " + str(n) + " nearest stations for pick-up are:")
    for i in range(n):
        print(i + 1, " - ", content[i]["title"], " - ", content[i]["subtitle"])

    print()

    favorite_pickup = int(0)
    print("You chose: ", content[favorite_pickup]["title"])
    print()

    """ -------------------------------------------------------------------------------------------------- """

    dropoffaddress = str(station_str)
    print("Your location for drop-off: ", dropoffaddress)
    n = 1
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(dropoffaddress) + '?format=json'

    location_response = requests.get(url).json()
    lat = location_response[0]["lat"]
    lon = location_response[0]["lon"]

    station_response = requests.get(
        "https://web-api.orange.sixt.com/v1/locations/geo?latitude=" + lat + "&longitude=" + lon)
    content = station_response.json()

    print()

    print("Your " + str(n) + " nearest stations for drop-off are:")
    for i in range(n):
        print(i + 1, " - ", content[i]["title"], " - ", content[i]["subtitle"])

    print()

    favorite_dropoff = int(0)
    print("You chose: ", content[favorite_dropoff]["title"])



    """ First loop is to define the exact pick up time """

    for SearchPickUpTimes in pickuptimes:
        for SearchDropoffTimes in dropofftimes:
            url = "https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=" + content[favorite_pickup]["id"] + "&returnStation=" + content[favorite_dropoff]["id"] + "&pickupDate=" + pickupdate_adbY + "T" + SearchPickUpTimes + "&returnDate=" + dropoffdate_adbY + "T" + SearchDropoffTimes + "&carType=car&campaign=default&currency=EUR&profileId="

            offer_response = requests.get(url)
            offer_content = offer_response.json()

            offers = offer_content["offers"]

            data = []
            nummer = 0

            df = pd.DataFrame(data)

            for x in offers:
                acrisscode = offer_content["offers"][nummer]["acrissCode"]
                cardescription = offer_content["offers"][nummer]["headlines"]["description"]
                mileage = offer_content["offers"][nummer]["mileageInfo"]["display"]
                price = offer_content["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"]
                priceindex = offer_content["offers"][nummer]["sortIndexes"]["price"]
                car_type = cardescription
                # print(nummer+1, ".", offer_content["offers"][nummer]["acrissCode"], offer_content["offers"][nummer]["headlines"]["description"], offer_content["offers"][nummer]["mileageInfo"]["display"], offer_content["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"])
                data.append(
                    {"cartype": car_type, "bookingclass": acrisscode, "cardescription": cardescription,
                     "mileage": mileage,
                     "pickupdate": pickupdate_adbY, "pickuptime": pickuptime_time, "dropofftime": dropofftime_time,
                     "dropoffdate": dropoffdate_date, "price": price, "searchid": searchid_int})

                df = pd.DataFrame(data)

                nummer += 1
                conn = sql.connect('/Users/johannes/PycharmProjects/sandbox_rentalscrape/RentalScrape/db.sqlite3')
                cursor = conn.cursor()
                df.to_sql('frontend_offer', conn, if_exists='replace', index_label='id')




            print("Success:", SearchPickUpTimes, SearchDropoffTimes)

