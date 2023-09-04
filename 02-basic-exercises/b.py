# INPUT = Time in minutes, OUTPUT = hours and minutes.
minutes = 123
hours = minutes // 60
minutes = minutes % 60
print("Hours: " + str(hours) + " Minutes: " + str(minutes))  # HOURS = 2, MINUTES = 3

# Same as above, but without using modulus (%).
minutes = 123
hours = minutes // 60
minutes = minutes - hours * 60
print("Hours: " + str(hours) + " Minutes: " + str(minutes))  # HOURS = 2, MINUTES = 3

# INPUT = Time in minutes, OUTPUT = hours, minutes, and seconds.
minutes = 123.5
hours = int(minutes // 60)
minutes = minutes % 60
seconds = minutes % 1 * 60
minutes = int(minutes)
print("Hours: " + str(hours) + " Minutes: " + str(minutes) + " Seconds: " + str(seconds))  # 02:03:30

# Same as above, but without using modulus (%).
minutes = 123.5
hours = int(minutes // 60)
minutes = minutes - hours * 60
seconds = (minutes - int(minutes)) * 60
minutes = int(minutes)
print("Hours: " + str(hours) + " Minutes: " + str(minutes) + " Seconds: " + str(seconds))  # 02:03:30
