import pandas_market_calendars as mcal
import pandas as pd
from app.holidays.exchange_mappings import eze_to_pandas



def check_holiday(market, date):

    market = eze_to_pandas.get(market, market)
    date = pd.to_datetime(date, format="%m/%d/%Y").normalize()
    print(market, date)

    try: 
        calendar = mcal.get_calendar(market)
    
        date = pd.Timestamp(date)
        return date in calendar.holidays().holidays
    except Exception as e:
        raise ValueError(f"Market '{market}' is not recognized.")