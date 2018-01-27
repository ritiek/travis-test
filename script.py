import datetime

today = datetime.date.today()
days_back = 10

time_travel_date = today - datetime.timedelta(days_back)
print(time_travel_date)
