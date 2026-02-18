
#* find number of odd days in a given year

def number_of_odd_days(year):
    days = 365
    if year%4 == 0:
        days = 366
    return days%7

print(number_of_odd_days(2004))