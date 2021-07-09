Weather Web Scraper
=======
Project Goal
---------------

The goal of this project was to collect historical weather data. Then the hope is to use various machine learning models to try and draw valuable insights from the large amount of data collected.

Steps and python folders 
-----------
Data scraping:

  * weather_webscraper.py
    1. This python file will scrape the weather of all cities or selected one's depending on the users input.
    2. Then  data is then saved in a csv file with the country and city in the name in the uncleaned data folder.
    3. Then the data is read back in and cleaned and saved in the cleaned data folder ready to be uploaded to the AWS RDS database.
  * Python to aws.py
    1. This python file appends each csv file to the database on AWS.

Imported Libaries
-----------   

1. selenium import webdriver
2. selenium.webdriver.common import keys
3. selenium.webdriver.common.keys import Keys
4. time import sleep
5. datetime import timedelta, datetime
6. pprint import pprint
7. import pandas as pd
8. import json

Amount of Data Scraped
----------------------

* 387 cities have been scraped
* Each city contains 12 years of weather data
* 4,568 rows per city
* 11 columns per city
* A total of 1,767,816 rows x 11 columns
