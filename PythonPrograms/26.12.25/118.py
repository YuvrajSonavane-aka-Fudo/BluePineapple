#convert a string to a list

def convert(str):
    try:
        return list(str)
    
    except:
        return "Invalid Input"

print(convert("abc"))