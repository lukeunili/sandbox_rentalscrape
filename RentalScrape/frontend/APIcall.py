import requests
import urllib.parse

pickupaddress = input("Where would you like to pick up your car? ")
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

dropoffaddress = input("Where would you like to drop off your car? ")
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

pickup_date = input('Enter a date in YYYY-MM-DD format: ')
print("Pickup-date", pickup_date)
print()
dropoff_date = input('Enter a date in YYYY-MM-DD format: ')
print("Dropoff-date:", dropoff_date)



url = "https://web-api.orange.sixt.com/v1/rentaloffers/offers?pickupStation=" + content[favorite_pickup]["id"] + "&returnStation=" + content[favorite_dropoff]["id"] + "&pickupDate=" + pickup_date + "T12:00:00&returnDate=" + dropoff_date + "T09:00:00&carType=car&campaign=default&currency=EUR&profileId="
print(url)
offer_response = requests.get(url)
offer_content = offer_response.json()

offers = offer_content["offers"]

#for key in offers:
    #print(key)

#offers = offer_content["offers"]

#print(offers)

nummer = 0

for x in offers:
    print(nummer+1, ".", offer_content["offers"][nummer]["acrissCode"], offer_content["offers"][nummer]["headlines"]["description"], offer_content["offers"][nummer]["mileageInfo"]["display"],  offer_content["offers"][nummer]["prices"]["totalPrice"]["amount"]["value"])
    nummer += 1

carselection = input('Which number would you like to select? ')
print("You selected number: ", carselection)
