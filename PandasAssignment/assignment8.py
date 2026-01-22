import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns
'''
For each customer:
sort by 
order_date 
compute 
prev_order_date
compute 
days_since_prev
compute rolling 3-order average net_amount 
Identify customers whose average order value is increasing (simple heuristic)
'''
data_frame = create_grossAmount_net_amount_value_columns()

def window_functions(data_frame):
    data_frame = data_frame.sort_values(['customer_id' , 'order_date'])
    data_frame['prev_order_date'] = data_frame.groupby('customer_id')['order_date'].shift(1)
    data_frame['days_since_prev'] = (data_frame['order_date'] - data_frame['prev_order_date']).dt.days
    data_frame['rolling_avg_3'] = (data_frame.groupby('customer_id')['net_amount'].transform(lambda x : x.rolling(window=3 , min_periods = 1).mean()))
    data_frame['is_improving']= data_frame.groupby('customer_id')['rolling_avg_3'].diff() > 0
    
    print(data_frame)

window_functions(data_frame)
