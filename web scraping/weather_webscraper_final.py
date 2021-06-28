#%%
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import timedelta, datetime

#choosing and ordering countries that want to be scraped
top_25_countries = ['Japan']#China','Germany','India', 'United Kingdom']#, 'France', 'Italy', 'Brazil', 'Canada', 'Russia', 'Australia', 'Spain', 'Saudi Arabia', 'Turkey', 'Switzerland', 'Poland', 'Thailand', 'Sweden', 'Nigeria', 'United States Of...', 'South Korea']
sorted_top_25_countries = sorted(top_25_countries)
url_of_top_25_countries = []

#opens the webpage of the website wanted to be scraped
driver = webdriver.Chrome()
driver.set_window_size(1920,1080)
driver.get('https://www.worldweatheronline.com/country.aspx')
sleep(2)

#finds the countries that want to be selected
url_of_weather_page = driver.find_elements_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[2]/div/div')
for element in url_of_weather_page:
    countrys = element.find_elements_by_xpath('.//ul/li')
    for country in countrys:
        for count in sorted_top_25_countries: 
            if country.text == count:
                url_of_top_25_countries.append(country.find_element_by_xpath('.//a').get_attribute('href'))

for url in url_of_top_25_countries:
    driver.get(url)
    url_of_capitals = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[2]/div[2]/dl/dd[1]/a').get_attribute('href')
    driver.get(url_of_capitals)    
    history = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[3]/a[2]')
    driver.execute_script("arguments[0].click();", history)
    date_button = driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_txtPastDate"]')
    driver.execute_script("arguments[0].click();", date_button)
    date_button.send_keys('01-01-2020')
    get_weather_button = driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')
    driver.execute_script("arguments[0].click();", get_weather_button)
    date_of_start = datetime.strptime('01-01-2020', '%d-%m-%Y')
    date_of_finish = datetime.strptime('05-01-2020','%d-%m-%Y')
    date_of_current_scrape = datetime.strptime('01-01-2020','%d-%m-%Y')
    print(date_of_current_scrape)
    delta = date_of_finish  - date_of_start
    delta = delta.days
    number_of_days_scraped = 0
    sleep(5)
    
    while number_of_days_scraped < delta:
        date_of_current_scrape += timedelta(days=1)
        date_of_current_scrape_formated = date_of_current_scrape.strftime('%d-%m-%Y')
        date_of_current_scrape_str = str(date_of_current_scrape_formated)
        print(date_of_current_scrape_str)
        date_button = driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_txtPastDate"]')
        driver.execute_script("arguments[0].click();", date_button)
        date_button.send_keys(date_of_current_scrape_str)
        get_weather_button = driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')
        driver.execute_script("arguments[0].click();", get_weather_button)
        sleep(2)
        number_of_days_scraped += 1


#%%
driver.quit()

# %%