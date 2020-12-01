from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from pandas import DataFrame



# specify the url
urlpage = 'https://www.sixt.de/mietwagen/deutschland/bayern/#/'
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
# execute script to scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 2s
time.sleep(2)
# click cookie button
cookie_button = driver.find_element_by_xpath("//*[@id='t3CookieCta']")
cookie_button.click()
time.sleep(1)
# click and enter text into rental station button
# Mobilerental_stationPicker = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/span')

Map = driver.find_element_by_xpath("//*[@id='contentpage']/body/main/section[4]/div/div/div/div[2]/div")
Map.click()

time.sleep(2)

StationList = driver.find_elements_by_class_name('inn')
data = []
for result in StationList:

    StationName = result.get_attribute('textContent')
    Station_Name = StationName.text

    #OpeningHours = result.find_element_by_class_name("station-open-hours")
    #for OH in OpeningHours:
    #    OpeningHoursScheduler = OH.find_element_by_class_name("opening-hours-scheduler")
    #    Opening_Hours = OpeningHoursScheduler.text




    data.append({"Station Name": Station_Name})

df = pd.DataFrame(data)
df.to_csv('firsttry.csv')


print(df)


print('Finish!')

driver.close()