from datetime import *
now = datetime.now()
# Get the current day, month, year, hour, minute and timestamp from datetime module
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(timestamp)
print("{}/{}/{}, {}:{}".format(day, month, year, hour, minute))

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_time)

# Today is 5 November, 2025. Change this time string to time.
time_string = "5 November, 2025"
time = datetime.strptime("5 November, 2025", "%d %B, %Y")
print(time)

# Calculate the time difference between now and new year.
new_year = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)
time_remaining = new_year - now
print("Time left for new year:", time_remaining)

# Calculate the time difference between 1 January 1970 and now.
unix_epoch = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
time_remaining = now - unix_epoch
print("Time passed after Unix Epoch:", time_remaining)