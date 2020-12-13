from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from pandas import DataFrame



# specify the url
urlpage = 'https://www.sixt.de/mietwagen/xml-sitemaps/branches.xml'
print(urlpage)
# run Chrome webdriver from executable path of your choice

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
#driver.set_window_size(800, 2000)

time.sleep(2)
#size = driver.get_window_size()

# get web page
driver.get(urlpage)


StationList = driver.find_elements_by_class_name("collapsible")
data = []
for result in StationList:

    StationName = result.find_element_by_class_name("collapsible-content")
    Station_Name = StationName.text

    data.append({"Station Name": Station_Name})

df = pd.DataFrame(data)
df.to_csv('firsttry.csv')

print(df)

print('Finish!')

driver.close()



# execute script to scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 2s
#time.sleep(2)
# click cookie button
#cookie_button = driver.find_element_by_xpath("//*[@id='t3CookieCta']")
#cookie_button.click()
#time.sleep(1)
# click and enter text into rental station button
# Mobilerental_stationPicker = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/span')




#data = []
#for result in StationList:

#    StationName = result.find_element_by_class_name("inn")
#    Station_Name = StationName.text
#    print(Station_Name)


    #OpeningHours = result.find_element_by_class_name("station-open-hours")
    #for OH in OpeningHours:
    #    OpeningHoursScheduler = OH.find_element_by_class_name("opening-hours-scheduler")
    #    Opening_Hours = OpeningHoursScheduler.text




#    data.append({"Station Name": Station_Name})

#df = pd.DataFrame(data)
#df.to_csv('firsttry.csv')


#print(df)


#print('Finish!')

#driver.close()