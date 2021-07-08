Weather Web Scraper
=======

Steps 
-----------
Data scraping:

  * weather_webscraper.py
    1. This python file will scrape the weather of all cities or selected one's depending on the users input.
    2. Then  data is then saved in a csv file with the country and city in the name in the uncleaned data folder.
    3. Then the data is read back in and cleaned ready to be uploaded to the AWS RDS database.
  * Python_to_sql
  1. This python file appends each csv file to the database on AWS.
