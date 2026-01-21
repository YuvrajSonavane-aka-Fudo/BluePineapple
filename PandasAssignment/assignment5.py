import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns

'''
Create a pivot:
index: month (from order_date )
columns: category
values: net_amount sum
Add a “Grand Totalˮ column and compute month-over-month growth %

'''
data_frame = create_grossAmount_net_amount_value_columns()

def create_pivot_table(data_frame):
    '''Returns a pivot table'''
    data_frame['Month'] = data_frame['order_date'].dt.to_period('M')

    pivot = data_frame.pivot_table(
        index = 'Month',
        columns = 'category',
        values = 'net_amount',
        aggfunc = 'sum',
        fill_value = 0,
        margins = True,
        margins_name = 'Grand Total'
    )
    pivot['MoM growth %'] = pivot['Grand Total'].pct_change()*100
    pivot = pivot.round(2)
    print(pivot)

create_pivot_table(data_frame)

