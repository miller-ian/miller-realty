from redfin_scraper import RedfinScraper

scraper = RedfinScraper()

scraper.setup("/Users/ianmiller/sources/buy_condo/zip_code_database.csv", False)

city_states = ["Arlington, Virginia",
               "Washington, DC",
               "Reston, Virginia"]
zip_codes = ["20009", "22302", "20170"]
sold = False
sale_period = None
lat_tuner = 1.5
lon_tuner = 1.5
scraper.scrape(city_states, 
               zip_codes, 
               sold, 
               sale_period, 
               lat_tuner, 
               lon_tuner)

print(scraper.get_data())