import time
import datetime

# print(time.strftime('%m/%d/%y'))

old_date = datetime.date(2016, 10, 1)
future_date = old_date + datetime.timedelta(days = 10)
print(future_date)


