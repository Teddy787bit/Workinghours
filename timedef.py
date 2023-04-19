import datetime

old_time = datetime.datetime.now()
new_time = old_time - datetime.timedelta(hours=2, minutes=10)
time_difference = divmod((old_time - new_time).total_seconds(),60)
print(time_difference)