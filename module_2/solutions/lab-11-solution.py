# 2.6.1.11

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

# this assumes that we aren't rolling time from 23:59 into a new day

total_time_in_minutes = (hour * 60) + mins + dura

hours = total_time_in_minutes // 60
minutes = total_time_in_minutes % 60

print(f"{hours}:{minutes}")