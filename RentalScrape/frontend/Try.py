import requests
import urllib.parse
import pandas as pd

#pickupaddress = input("Where would you like to pick up your car? ")
#print("Your location for pick-up: ", pickupaddress)
n = 3
#url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(pickupaddress) +'?format=json'

#location_response = requests.get(url).json()
lat = "48.354249660166296"
lon = "11.784820800992158"

station_response = requests.get("https://web-api.orange.sixt.com/v1/locations/geo?latitude=" + lat + "&longitude=" + lon)
content = station_response.json()

print()

print("Your " + str(n) + " nearest stations for pick-up are:")
for i in range(n):
    print(i+1, " - ", content[i]["title"], " - ", content[i]["subtitle"])

print()

favorite_pickup = int(input("Choose the desired # of your pick-station: ")) - 1
print("You chose: ", content[favorite_pickup]["title"])
print()

""" -------------------------------------------------------------------------------------------------- """

dropoffaddress = favorite_pickup
#print("Your location for drop-off: ", dropoffaddress)
n = 5
#url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(dropoffaddress) +'?format=json'

#location_response = requests.get(url).json()
#lat = location_response[0]["lat"]
#lon = location_response[0]["lon"]

station_response = requests.get("https://web-api.orange.sixt.com/v1/locations/geo?latitude=" + lat + "&longitude=" + lon)
content = station_response.json()

print()

print("Your " + str(n) + " nearest stations for drop-off are:")
for i in range(n):
    print(i+1, " - ", content[i]["title"], " - ", content[i]["subtitle"])

print()

favorite_dropoff = favorite_pickup
print("You chose: ", content[favorite_dropoff]["title"])

pickup_date = "2021-04-10"
print("Pickup-date", pickup_date)

return_date = "2021-04-13"
print("Return-date:", return_date)

pickup_time = "09:00:00"
print("Pickup time:", pickup_time)

return_time = "09:00:00"
print("Return time:", return_time)

url = "https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=" + content[favorite_pickup]["id"] + "&returnStation=" + content[favorite_dropoff]["id"] + "&pickupDate=" + pickup_date + "T" + pickup_time + "&returnDate=" + return_date + "T" + return_time + "&carType=car&campaign=default&currency=EUR&profileId="
print(url)
offer_response = requests.get(url)
offer_content = offer_response.json()

offers = offer_content["offers"]

#for key in offers:
    #print(key)

#offers = offer_content["offers"]

#print(offers)

nummer = 0

data = []

for x in offers:
    acrisscode = offer_content["offers"][nummer]["acrissCode"]
    cardescription = offer_content["offers"][nummer]["headlines"]["description"]
    mileage = offer_content["offers"][nummer]["mileageInfo"]["display"]
    price = offer_content["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"]
    priceindex = offer_content["offers"][nummer]["sortIndexes"]["price"]
    #print(nummer+1, ".", offer_content["offers"][nummer]["acrissCode"], offer_content["offers"][nummer]["headlines"]["description"], offer_content["offers"][nummer]["mileageInfo"]["display"], offer_content["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"])
    data.append(
        {"acrisscode": acrisscode, "cardescription": cardescription, "priceindex": priceindex, "mileage": mileage,
         "pickup_date": pickup_date, "pickup_time": pickup_time, "return_time": return_time, "return_date": return_date, "price": price})
    df = pd.DataFrame(data)

    nummer += 1

print(df.sort_values(by="price"))

carselection = input('Which ACRISS Code would you like to select? ')
print("You selected ACRISS Code: ", carselection)

url = "https://www.sixt.de/php/reservation/directoffer?uci=" + content[favorite_pickup]["id"][2:] + "&rci=" + content[favorite_dropoff]["id"][2:] + "&uda=" + pickup_date + "&rda=" + return_date + "&uti=" + pickup_time + "&rti=" + pickup_time + "&ctyp=P&grp=" + carselection + "&kdnr=&pasw="

print(url)
