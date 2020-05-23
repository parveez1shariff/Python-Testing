from datetime import datetime, timedelta
now = datetime.now()
then = datetime(1985,12,20)

delta = now-then

print(delta.days)
print(delta.seconds)

def get_n_days_after_date(date_format = "%d %B %Y", add_days=120):
    date_n_days_after = datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

get_n_days_after_date(date_format = 1  3)
