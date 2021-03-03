import datetime

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.hour)
print(now + datetime.timedelta(days=28))
