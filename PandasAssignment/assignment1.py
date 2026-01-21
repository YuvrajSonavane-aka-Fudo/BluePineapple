import pandas as pd
'''
Create a DataFrame from a dict (at least 10 rows).
Show 
.head() , 
.info() , 
.describe(include="all") .
Convert a date column to datetime.
Trim whitespace from string columns.
'''

dict1 = {
    
    "ID":[1,2,3,4,5,6,7,8,9,10],
    "Name" : ["a ","b","c ","d ","e","f","g","h","i","j"],
    "Date" : ['1-1-2026' ,'2-1-2026' , '3-1-2026' , '4-1-2026' , '5-1-2026' ,'6-1-2026','7-1-2026','8-1-2026','9-1-2026','10-1-2026'  ]

}

data_frame = pd.DataFrame(dict1)
print(f"The head is ->\n {data_frame.head()}\n")

data_frame.info()

print(f"The description is ->\n {data_frame.describe(include="all")}")

data_frame["Date"] = pd.to_datetime(data_frame['Date'])
print(data_frame)

data_frame["Name"] = data_frame["Name"].str.strip()
print(data_frame)



