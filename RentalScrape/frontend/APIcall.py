import requests
import urllib.parse

pickupaddress = "Graz" #input("Where would you like to pick up your car? ")
print("Your location for pick-up: ", pickupaddress)
n = 3
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(pickupaddress) +'?format=json'

location_response = requests.get(url).json()
lat = location_response[0]["lat"]
lon = location_response[0]["lon"]

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

dropoffaddress = "Graz" #input("Where would you like to drop off your car? ")
print("Your location for drop-off: ", dropoffaddress)
n = 5
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(dropoffaddress) +'?format=json'

location_response = requests.get(url).json()
lat = location_response[0]["lat"]
lon = location_response[0]["lon"]

station_response = requests.get("https://web-api.orange.sixt.com/v1/locations/geo?latitude=" + lat + "&longitude=" + lon)
content = station_response.json()

print()

print("Your " + str(n) + " nearest stations for drop-off are:")
for i in range(n):
    print(i+1, " - ", content[i]["title"], " - ", content[i]["subtitle"])

print()

favorite_dropoff = int(input("Choose the desired # of your dropoff-station: ")) - 1
print("You chose: ", content[favorite_dropoff]["title"])

pickup_date = "2021-03-26" #input('Enter a date in YYYY-MM-DD format: ')
print("Pickup-date", pickup_date)
print()
dropoff_date = "2021-03-28" #input('Enter a date in YYYY-MM-DD format: ')
print("Dropoff-date:", dropoff_date)



url = "https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=" + content[favorite_pickup]["id"] + "&returnStation=" + content[favorite_dropoff]["id"] + "&pickupDate=" + pickup_date + "T12:00:00&returnDate=" + dropoff_date + "T09:00:00&carType=car&campaign=default&currency=EUR&profileId="
print(url)
offer_response = requests.get(url)
offer_content = offer_response.json()

offers = offer_content["offers"]

for key in offers:
    print(key)