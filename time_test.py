import datetime

offset = datetime.timezone(datetime.timedelta(hours=3))

now_time = datetime.datetime.now(offset)

print(now_time.hour)