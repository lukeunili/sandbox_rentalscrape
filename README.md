#### RentalScrape

##### Introduction
RentalScrape is an app that enables users to easily look for multiple different time-combinations for renting SIXT rental cars. We allow users to define a two hour time window in which they could pick-up and drop-off their rental car. By analyzing all possible time combinations, we suggest the user the cheapest combination of times possible.

##### Functioning
The user is asked to choose a Station, Pick-up date as well as Drop-Off date. In addition, we're asking for a time frame in which the user can pick up and drop off the car. If the user for example is able to pick up between 08:30 and 10:00 and drop-off between 21:00 and 22:00, RentalScrape calculates time-combinations like 08:30, 21:00; 08:30, 21:30; 08:30, 22:00; 09:00, 21:00 and so on. In a second step, a Selenium-based scraper is used to silently loop through all combinations and scrape SIXT' website and write all offers to an sqlite table. Once the scraping is finished and all results are saved to the sqlite table, the user will be presented with all results order ascending.  

##### Common issues
From time to time, sixt.at is not responding in a timely manner or broken in general. In this case, the scraping will display errors.
Rarely, some prices are not written to the database correctly.

##### Necessary apps
Selenium<br>
Chromedriver<br>
Pandas<br>

