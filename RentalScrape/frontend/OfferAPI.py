import pandas as pd
import sqlite3 as sql
import datetime as datetime
import locale
import requests
import time


def convertTuple(tup):
    str = ''.join(tup)
    return str

'''class SQLData:
    """ -- CREATING PICKUPTIME LIST -- """

    conn = sql.connect('../frontend/db.sqlite3')
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

    pickuptime0_str = pickuptime0.strftime("%H:%M")
    pickuptimes.append(pickuptime0_str)
    pickuptime30_str = pickuptime30.strftime("%H:%M")
    pickuptimes.append(pickuptime30_str)
    pickuptime60_str = pickuptime60.strftime("%H:%M")
    pickuptimes.append(pickuptime60_str)
    pickuptime90_str = pickuptime90.strftime("%H:%M")
    pickuptimes.append(pickuptime90_str)
    pickuptime120_str = pickuptime120.strftime("%H:%M")
    pickuptimes.append(pickuptime120_str)
    """Append all possible pickuptimes to list"""

    print("Pickuptimes:")
    print(pickuptimes)


    """ -- CREATING returntime_timeTIME LIST -- """

    conn = sql.connect('../frontend/db.sqlite3')
    cursor2 = conn.cursor()
    accessreturntime_timetime = ("SELECT substr(returntime_timetimestart,1,5) FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor2.execute(accessreturntime_timetime)
    returntime_timetimestart_tuple = cursor2.fetchone()
    cursor2.close()
    """Connect to sqlite table and fetch returntime_timetime as tuple"""

    returntime_timetimestart_str = convertTuple(returntime_timetimestart_tuple)
    """Convert tuple into string"""

    returntime_timetime_time = datetime.datetime.strptime(returntime_timetimestart_str, "%H:%M")
    """Convert string into datetime format"""

    returntime_timetime0 = returntime_timetime_time
    returntime_timetime30 = returntime_timetime_time + datetime.timedelta(hours=0, minutes=30, seconds=0)
    returntime_timetime60 = returntime_timetime_time + datetime.timedelta(hours=1, minutes=00, seconds=0)
    returntime_timetime90 = returntime_timetime_time + datetime.timedelta(hours=1, minutes=30, seconds=0)
    returntime_timetime120 = returntime_timetime_time + datetime.timedelta(hours=2, minutes=00, seconds=0)
    """Add hr:mm to first returntime_timetime to create 2 hr window"""

    returntime_timetimes = []
    """Create returntime_timetimes list"""

    returntime_timetime0_str = returntime_timetime0.strftime("%H:%M")
    returntime_timetimes.append(returntime_timetime0_str)
    returntime_timetime30_str = returntime_timetime30.strftime("%H:%M")
    returntime_timetimes.append(returntime_timetime30_str)
    returntime_timetime60_str = returntime_timetime60.strftime("%H:%M")
    returntime_timetimes.append(returntime_timetime60_str)
    returntime_timetime90_str = returntime_timetime90.strftime("%H:%M")
    returntime_timetimes.append(returntime_timetime90_str)
    returntime_timetime120_str = returntime_timetime120.strftime("%H:%M")
    returntime_timetimes.append(returntime_timetime120_str)
    """Append all possible returntime_timetimes to list"""

    print("returntime_timetimes:")
    print(returntime_timetimes)

    """ -- DEFINING STATION -- """

    conn = sql.connect('../frontend/db.sqlite3')
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

    conn = sql.connect('../frontend/db.sqlite3')
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

    pickupdate_adbY = pickupdate_date.strftime("%a. %-d. %b %Y")
    print("Pick-up date:")
    print(pickupdate_adbY)


    """ -- DEFINING returntime_timeDATE -- """

    locale.setlocale(locale.LC_ALL, 'de_DE')
    """Set local settings to use german days and months"""

    conn = sql.connect('../frontend/db.sqlite3')
    cursor5 = conn.cursor()
    accessreturntime_timedate = ("SELECT returntime_timedate FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor5.execute(accessreturntime_timedate)
    returntime_timedate_tuple = cursor5.fetchone()
    cursor5.close()
    """Connect to sqlite table and fetch returntime_timedate as tuple"""

    returntime_timedate_str = convertTuple(returntime_timedate_tuple)
    """Convert tuple into string"""

    returntime_timedate_date = datetime.datetime.strptime(returntime_timedate_str, "%Y-%m-%d")
    """Convert string into datetime format"""

    returntime_timedate_adbY = returntime_timedate_date.strftime("%a. %-d. %b %Y")

    print("Drop-off date:")
    print(returntime_timedate_adbY)


    """ -- DEFINING SEARCHID -- """

    conn = sql.connect('../frontend/db.sqlite3')
    cursor6 = conn.cursor()
    accesssearchid = ("SELECT id FROM frontend_searchinput ORDER BY id DESC LIMIT 1")
    cursor6.execute(accesssearchid)
    searchid_tuple = cursor6.fetchone()
    cursor6.close()
    """Connect to sqlite table and fetch searchid as tuple"""

    searchid_int = sum(searchid_tuple)
    """Convert tuple into integer"""

    print("Search ID:")
    print(searchid_int)'''

PickupStationID = "11"
ReturnStationID = "11"
PickupDate = "2021-04-10"
ReturnDate = "2021-04-12"
PickupTime = "09:00:00"
ReturnTime = "09:00:00"

SixtOfferURL = 'https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=' + PickupStationID + '&returnStation=' + ReturnStationID + '&pickupDate=' + PickupDate + 'T' + PickupTime + '&returnDate=' + ReturnDate + 'T' + ReturnTime + '&carType=car&campaign=default&currency=EUR&profileId='


r = requests.get(SixtOfferURL)

offercontent = r.json()

offers = offercontent["offers"]

#print(offers)

nummer = 0

for x in offers:
    print(offercontent["offers"][nummer]["acrissCode"], offercontent["offers"][nummer]["headlines"]["description"], offercontent["offers"][nummer]["mileageInfo"]["display"],  offercontent["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"])
    nummer += 1


#for key in offers:
#    print(key)

#print(offercontent["offers"][0]["prices"]["totalPrice"]["amount"]["value"])