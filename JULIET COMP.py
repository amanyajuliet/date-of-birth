import datetime,calendar
current_year = 2017
date = input("Enter your date of birth (1-31)\n")
endings = ["st","nd","rd"] + 17*["th"]+ ["st","nd","rd"] + 7*["th"] + ["st"]
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY',
        'FRIDAY','SATURDAY','SUNDAY']

month = int(input("Enter the month in which you were born (1-12)\n"))
month_names = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY',
               'JUNE', 'JULY', 'AUGUST', 'SEMPTEMBER', 'OCTOBER',
               'NOVEMBER', 'DECEMBER']
year = int(input("What's your age?\n"))
M = month_names[month-1]
D = int(date)
Y = (current_year-year)
D1 = date+endings[D-1]
C = calendar.weekday(Y,month,D)
D2 = days[C]

this = M+" ", D, ",", Y
print("woow you were born on ",D2,D1,M, "of the year",Y)
