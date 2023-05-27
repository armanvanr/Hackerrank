def dayOfProgrammer(year):
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
    elif 1919 <= year <= 2700:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            date = "12.09." + str(year)
        else:
            date = "13.09." + str(year)
    else:
        date = "26.09." + str(year)
    return date


def dop(year):
    date = "13.09." + str(year)
    if 1700 <= year <= 1917 and year % 4 == 0:
        date = "12.09." + str(year)
    elif 1919 <= year <= 2700:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            date = "12.09." + str(year)
    else:
        date = "26.09." + str(year)
    return date


print(dayOfProgrammer(1918))
# notes:
# in regular years, DOTP is on 13 September
# in leap years of Julian and Gregorian Calendars, DOTP is on 12 September
# in transition 1918, DOTP is on 26 September

# Julian leap years: "multiply of 4" e.g. 1700, 1704, 1708, ...

# Gregorian leap years: "multiply of 400" e.g. 2000 and 2400
# or "multiply of 4 and not multiply of 100"
# e.g. 1920, 1924, 1928 ... (2100, 2200, 2300 not included)

# 1918 is not a leap year
