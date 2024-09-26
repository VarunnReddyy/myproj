from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_future_date(months=0, weeks=0, hour=0):
    now = datetime.now()
    future_date = now + relativedelta(months=months, weeks=weeks, hour=hour)
    return future_date

