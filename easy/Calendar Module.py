import calendar
mm, dd, yyyy = map(int, input().split())
print(calendar.day_name[calendar.weekday(yyyy,mm,dd)].upper())
