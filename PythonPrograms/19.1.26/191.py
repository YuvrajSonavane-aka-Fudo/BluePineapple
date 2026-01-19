
#* check whether the given month contains 30 days or not

def is_30_day_month(str1):
    '''Accepts a string . Checks whether that it is a 30 day month or not'''
    thirty_day_months = ["april","june","september" , "november"]
    str1 = str1.lower()
    if str1 in thirty_day_months:
        return True
    return False

print(is_30_day_month("January"))