import calendar, time
print("Time Conversion",calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S')))
