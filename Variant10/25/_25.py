minute = 60
hour = 3600
day = 86400
seconds = int(input("input number of seconds: "))
days = seconds / day
seconds = seconds % day
hours = seconds / hour
seconds = seconds % hour
minutes = seconds / minute
seconds = seconds % minute
print("result:", \
 "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))
