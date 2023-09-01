# miller-realty

## Usage

```
git clone git@github.com:miller-ian/miller-realty.git
cd miller-realty
python3 scrape.py
```

Estimated monthly payments will print out to the console on the right-most column of the screen.

"Monthly payment" is the total amount you will spend on this asset. This includes mortgage payment, HOA fee, and estimated property management fee.

## Variables

The monthly payment estimation assumes several variables. You can change these depending on your specific situation.

1. "available_down_payment" = the size of your down payment
2. "list_price_discount" = how much you believe you can negotiate down the price of the unit
3. "interest_rate" = annual rate on loan
4. "biweekly" = "True" if you are planning on making payments every 2 weeks, "False" if you are planning on making a single payment each month
