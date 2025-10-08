# Task - 1
from datetime import date, timedelta

current_date = date.today()
new_date = current_date - timedelta(days=5)

print("Current data:", current_date)
print("Data - 5 days: ", new_date)

# Task - 2
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Today is: ", today)
print("Yesterday was: ", yesterday)
print("Tomorrow will be: ", tomorrow)

# Task - 3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("С микросекундами:", now)
print("Без микросекунд:", no_microseconds)

# Task - 4
date1 = date.today()
date2 = date1 + timedelta(days=1)

difference = date2 - date1
seconds = difference.total_seconds()

print("Разница между датами:", difference)
print("Разница в секундах:", seconds)