from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
print("Current date and time:", now)

future_date = now + relativedelta(months=1, weeks=1, hour=10)
print("Future date and time:", future_date)
