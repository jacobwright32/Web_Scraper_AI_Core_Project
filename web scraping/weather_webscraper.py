#%%
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import timedelta, datetime
from pprint import pprint
import pandas as pd
import json

list_of_all_countries = []
url_of_all_countries = []
name_and_url_of_all_countries = {}
list_of_cities = []
url_list_of_cities = []
dictionary_of_url_and_name = {}
all_city_weather = {}
list_of_file_names = []


class WebScraper:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920,1080)
    
    def website_search(self):
        self.driver.get('https://www.worldweatheronline.com/country.aspx')
        sleep(2)
    
    def gets_user_list_of_countries(self):
        user_input = input('\n\nIf you would like a list of the countries enter "yes": ')
        
        url_of_weather_page = self.driver.find_elements_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[2]/div/div')
        
        for element in url_of_weather_page:
            countrys = element.find_elements_by_xpath('.//ul/li')
            
            for country in countrys:
                name_and_url_of_all_countries[country.text] = country.find_element_by_xpath('.//a').get_attribute('href')
                list_of_all_countries.append(country.text)
                url_of_all_countries.append(country.find_element_by_xpath('.//a').get_attribute('href'))

        if user_input == 'yes':
            pprint(list_of_all_countries)
        
        else:
            print('')
    
    def user_country_selector(self):
        self.country_selector = input('\nEnter a country you want to scrape\n Multiple entries allowed\nType "last_save" to continue previous scrape\n Type "done" to start the scrape or "all" to scrape all countries: ')
        url_of_selected_countries = []

        while self.country_selector != 'done' or self.country_selector != 'all' or self.country_selector != 2:
            
            if self.country_selector.lower() == 'all':
                url_of_selected_countries = url_of_all_countries
                break
            
            elif self.country_selector.lower() == 'done':
                break
            
            elif self.country_selector.lower() == 'last_save':
                url_of_selected_countries = ['https://www.worldweatheronline.com/united-kingdom-weather.aspx']
                break
            else:
                url_of_selected_countries.append(name_and_url_of_all_countries[self.country_selector])
                self.country_selector = input('\nEnter a country you want to scrape or write done to start: ')
        
        return self.country_selector, url_of_selected_countries  
    
    def gets_each_countries_major_cities_name_and_url(self):
        
        for url in url_list_of_all_selected_countries:
            self.driver.get(url)
            major_cities_of_current_country = self.driver.find_elements_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[5]/div[1]/div/ul/li')       # url_of_capitals = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[2]/div[2]/dl/dd[1]/a').get_attribute('href')
            
            if len(major_cities_of_current_country) == 0:
                major_cities_of_current_country = self.driver.find_elements_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[1]/div/div/div[4]/div[1]/div/ul/li')

            else: 
                major_cities_of_current_country = major_cities_of_current_country
            
            for city in major_cities_of_current_country:
                    url_list_of_cities.append(city.find_element_by_xpath('.//a').get_attribute('href'))
                    list_of_cities.append(city.text)
                    dictionary_of_url_and_name[city.text] = city.find_element_by_xpath('.//a').get_attribute('href')
            
        return dictionary_of_url_and_name, url_list_of_cities, list_of_cities

    def city_scraper(self):
        x = 0
        self.city_done = 0
        total_days_done = 0
        
        for url in urls:
            self.driver.get(url)
            
            history = self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[3]/div[3]/a[2]')
            self.driver.execute_script("arguments[0].click();", history)
            
            date_button = self.driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_txtPastDate"]')
            self.driver.execute_script("arguments[0].click();", date_button)
            date_button.send_keys('01-01-2020')
            
            get_weather_button = self.driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')
            self.driver.execute_script("arguments[0].click();", get_weather_button)
            
            date_of_current_scrape = datetime.strptime('01-01-2020','%d-%m-%Y')
            date_of_finish = datetime.strptime('31-12-2020','%d-%m-%Y')

            delta = date_of_finish  - date_of_current_scrape
            delta = delta.days

            self.name_of_city = self.driver.find_element_by_class_name('top_title').text
            self.name_of_country = self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[2]/nav/ol/li[3]/a').text 
            all_city_weather[self.name_of_city] = {}

            days_done = 0
            number_of_days_scraped = 0
            

            while number_of_days_scraped <= delta:
                all_weather_data = self.driver.find_elements_by_xpath('//*[@id="aspnetForm"]/div[4]/main/div[4]/div[1]/div[5]/div/div[2]')
                print('Days Done: '+ str(days_done) + '/' + str(delta) + ' Cities Done: ' + str(self.city_done) + '/' + str(len(urls)) + ' | ' + str(round(total_days_done / (len(urls) * delta) * 100, 2)) + '% Percentage Complete' + ' | Total Percentage of all countries scraped: ' + str(round(((8639-len(number_of_cities_left))/8639)*100,2)) + '%')

                for weather in all_weather_data:
                    list_of_weather_data = weather.text.split('\n')
                    del list_of_weather_data[0:9]
                    x = 0
                    
                    while x < len(list_of_weather_data)/9: 
                        all_weather_data = {
                                list_of_weather_data[(x*9)] + '-' + date_of_current_scrape.__format__('%m-%d') : {
                        'Country' : self.name_of_country,
                            'City' : self.name_of_city,
                                'Maximum Temprature' : list_of_weather_data[(x*9)+1],
                                    'Minimum Temprature' : list_of_weather_data[(x*9)+2],
                                        'Wind Speed' : list_of_weather_data[(x*9)+3],
                                            'Wind Direction' : list_of_weather_data[(x*9)+4],
                                                'Amount of Rain' : list_of_weather_data[(x*9)+5],
                                                    'Humidity' : list_of_weather_data[(x*9)+6],
                                                        'Cloud coverage' : list_of_weather_data[(x*9)+7],	
                                                        'Pressure' : list_of_weather_data[(x*9)+8]
                        }}
                        
                        all_city_weather[self.name_of_city].update(all_weather_data)
                        x += 1      
                date_of_current_scrape += timedelta(days=1)
                date_of_current_scrape_str = str(date_of_current_scrape.strftime('%d-%m-%Y'))
                date_button = self.driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_txtPastDate"]')
                self.driver.execute_script("arguments[0].click();", date_button)
                date_button.send_keys(date_of_current_scrape_str)
                get_weather_button = self.driver.find_element_by_xpath('//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')
                self.driver.execute_script("arguments[0].click();", get_weather_button)
                number_of_days_scraped += 1
                days_done += 1
                total_days_done += 1

            scrape.saves_file_to_csv_and_cleans()
            self.city_done += 1
            del number_of_cities_left[0]
            with open('List_of_cites_left.json', 'w') as f:
                json.dump(number_of_cities_left, f)
            print(len(number_of_cities_left))

    def saves_file_to_csv_and_cleans(self):
            df = pd.DataFrame(all_city_weather[self.name_of_city])
            df.to_csv('Uncleaned Data/' + self.name_of_country + '_' + self.name_of_city + '.csv', index=True)
            self.file_name = (str(self.name_of_country + '_' + self.name_of_city))
            self.df = pd.read_csv('Uncleaned Data/' + self.file_name +'.csv')
            df = self.df.T
            df.sort_index(inplace=True)
            df = df.rename(columns={ 0: 'country', 1: 'city', 2: 'maximum_temprature', 3: 'minimum_temprature', 4: 'wind_speed', 5: 'wind_direction', 6: 'amount_of_rain', 7:'humidity', 8: 'cloud_coverage', 9:'pressure'})    
            df.drop(df.tail(1).index,inplace=True)
            df['maximum_temprature'] = df['maximum_temprature'].str.replace(' °c', '')
            df['minimum_temprature'] = df['minimum_temprature'].str.replace(' °c', '')
            df['Wind_Speed'] = df['Wind_Speed'].str.replace(' km/h', '')
            df['amount_of_rain'] = df['amount_of_rain'].str.replace(' mm', '')
            df['humidity'] = df['humidity'].str.replace('%', '')
            df['cloud_coverage'] = df['cloud_coverage'].str.replace('%', '')
            df['pressure'] = df['pressure'].str.replace(' mb', '') 
            df.index.name = 'date'
            df.to_csv('Cleaned Data/' + self.file_name + '_Cleaned.csv')
        

    def close_webpage(self):
        self.driver.quit()

scrape = WebScraper()
scrape.website_search()
scrape.gets_user_list_of_countries()
last_save, url_list_of_all_selected_countries = scrape.user_country_selector()
dictionary_of_url_and_names, urls, names = scrape.gets_each_countries_major_cities_name_and_url()
if last_save == 'last_save':
    with open("List_of_cites_left.json", 'r') as rf:
        urls = json.load(rf)
else:
    number_of_cities_left = urls.copy()
    with open('List_of_cites_left.json', 'w') as f:
        json.dump(number_of_cities_left, f)


number_of_cities_left = urls.copy()
scrape.city_scraper()
scrape.close_webpage()
#%%

