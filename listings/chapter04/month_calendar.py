from datetime import date
from sys import argv

if len(argv) > 2:
    year = int(argv[1])
    month = int(argv[2])
    if len(argv) > 3:
        day = int(argv[3])
    else:
        day = 1
else:
    today = date.today()
    day = today.day
    month = today.month
    year = today.year

first_of_month = date(year, month, 1)
weekday = first_of_month.weekday()
month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_lengths[1] = 29

print("{:02d}/{}".format(month, year))
print(" Mo  Di  Mi  Do  Fr  Sa  So")
print(' ' * weekday * 4, end = '')
for d in range(1, month_lengths[month - 1] + 1):
    if d == day:
        print("[{:2d}]".format(d), end = '')
    else:
        print(" {:2d} ".format(d), end = '')
    weekday += 1
    if weekday % 7 == 0:
        weekday = 0
        print()
print()
