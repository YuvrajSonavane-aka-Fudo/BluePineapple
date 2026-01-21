import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns

'''
Create a customers DataFrame: 
Merge with orders.
customer_id , 
signup_date , 
segment .
Compute revenue by segment and retention proxy:
“active in last 60 daysˮ per segment.
'''

order_df = create_grossAmount_net_amount_value_columns()

def revenue_by_segment(order_df):
    customer_df = pd.read_csv('customers.csv')
    customer_df['signup_date'] = pd.to_datetime(customer_df['signup_date'])

    merged_df = pd.merge(order_df,customer_df,on= "customer_id" , how='left')

    latest_date = merged_df['order_date'].max()
    merged_df['active last 60 days'] = (latest_date - merged_df['order_date']).dt.days <= 60

    segment_analysis = merged_df.groupby('segment').agg(
        total_revenue = ('net_amount' , 'sum'),
        total_order = ('order_id','count'),
        active_customers = ('active last 60 days','sum')
    ).round(2)

    segment_analysis['retention%'] = (segment_analysis['active_customers'] / segment_analysis['total_order'])*100

    print(segment_analysis)

revenue_by_segment(order_df)

