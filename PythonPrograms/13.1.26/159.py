
#! print season for given month and day

def print_season(month , day):
    summerMonths = ["feb" , "march" , "april" , "may"]
    monsoonMonths = ["june" , "july"]
    autumnMonths = ["august" , "september" , "october"]
    winterMonths = ["november" , "december" , "january"]

    if month.lower() in summerMonths:
        return "Summer"

    if month.lower() in monsoonMonths:
        return "Monsoon"
    
    if month.lower() in autumnMonths:
        return "Autumn"

    if month.lower() in winterMonths:
        return "Winter"

print(print_season("january", "Monday"))

