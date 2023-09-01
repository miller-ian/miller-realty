from redfin_scraper import RedfinScraper

available_down_payment = 60000
list_price_discount = 10 # in percentage points

def calculate_monthly_payment(list_price, hoa):

    list_price = list_price*(1 - list_price_discount / 100) #
    principal = float(float(list_price) - available_down_payment)
    interest_rate = 7
    loan_term = 30

    r = interest_rate / 100 / 12
    loan_term_months = loan_term * 12
    n = loan_term * 26 #assuming biweekly payments

    # Calculate monthly mortgage payment
    monthly_payment = (principal * r * ((1+r)**n)) / (((1+r)**n) - 1)

    total_monthly_payment = (monthly_payment + float(hoa)) * 1.1 #1.1x is property management fee estimate

    total_payment = (monthly_payment * loan_term_months)
    return total_monthly_payment

def scrape():

    scraper = RedfinScraper()

    scraper.setup("/Users/ianmiller/sources/projects/miller-realty/zip_code_database.csv", False)

    units_of_interest = [
        "2337 Champlain St NW #1",
        "1800 Key Blvd #500",
        "1301 N Courthouse Rd #1114",
    ]

    city_states = ["Arlington, Virginia",
                "Washington, DC",
                ]
    zip_codes = ["20009", "22302", "20170", "22201"]
    sold = False
    sale_period = None
    lat_tuner = 3
    lon_tuner = 3
    scraper.scrape(city_states, 
                zip_codes, 
                sold, 
                sale_period, 
                lat_tuner, 
                lon_tuner)

    scrape_data = scraper.get_data()
    uoi_data = scrape_data[scrape_data['ADDRESS'].isin(units_of_interest)]

    uoi_data["Ian's Estimated Monthly Payment"] = uoi_data.apply(lambda x: calculate_monthly_payment(x["PRICE"], x["HOA/MONTH"]), axis=1)
    return uoi_data

if __name__ == "__main__":
    df = scrape()
    print(df)