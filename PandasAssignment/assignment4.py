import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns
'''
Group by 
city and compute:
total orders
unique customers
total revenue (sum net_amount)
average order value
Sort by 
revenue desc and show top 10 cities 
'''
data_frame = create_grossAmount_net_amount_value_columns()

def group_by_aggregate_functions(data_frame):
    '''Returns a data frame grouped by the some aggregate functions '''
    grouped_data_frame = data_frame.groupby("city").agg(
        total_orders = ("order_id","count"),
        unique_customers = ('customer_id','nunique'),
        total_revenue = ('net_amount','sum'),
        avg_revenue = ('net_amount','mean'),

    ).nlargest(10,'total_revenue').round(2)

    print(grouped_data_frame)

    return grouped_data_frame

group_by_aggregate_functions(data_frame)