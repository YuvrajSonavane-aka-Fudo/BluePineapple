import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns

'''
Importing the assignment 2 dataframe as well for simplicity
Filter orders:
category in a set (e.g., Electronics/Fashion)
net_amount > X
order_date within last N days (relative to 
Output 
count + total net_amount .
'''

data_frame = create_grossAmount_net_amount_value_columns()

def filtered_data(data_frame):
    '''Filters data and returns the filtered data frame , total count and total net_amount sum in a list'''
    
    category = {"Electronics" , "Fashion"}
    X = 500
    last_n_days = 30

    latest_date = data_frame['order_date'].max()
    cutoff_date = latest_date - pd.Timedelta(days = last_n_days)

    filtered_data_frame = data_frame[
        (data_frame['category'].isin(category))&
        (data_frame["net_amount"]>=X)&
        (data_frame['order_date']>=cutoff_date)
    ]
    count = len(filtered_data_frame)
    total_net_amout = filtered_data_frame['net_amount'].sum()

    return [filtered_data_frame , count , total_net_amout]
    

print(filtered_data(data_frame))



