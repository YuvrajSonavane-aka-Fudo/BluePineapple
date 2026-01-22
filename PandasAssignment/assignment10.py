import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns

'''
Define cohort month = customerʼs first order month.
For each cohort, compute:
number of active customers by month offset M0, M1, M2…)
retention rate matrix (cohort table)
Output as a DataFrame shaped like a retention heatmap table (values as 
%
'''
data_frame = create_grossAmount_net_amount_value_columns()
def cohort_month(data_frame):

    # 1. Truncate dates to monthly periods
    data_frame['order_date'] = pd.to_datetime(data_frame['order_date']) 
    data_frame['order_month'] = data_frame['order_date'].dt.to_period('M')

    # 2. Define cohort month for each customer
    data_frame['cohort_month'] = data_frame.groupby('customer_id')['order_date'].transform('min').dt.to_period('M')

    # 3. Calculate month offset using year and month components
    def calculate_offset(row):
        years_diff = row['order_month'].year - row['cohort_month'].year
        months_diff = row['order_month'].month - row['cohort_month'].month
        return (years_diff * 12) + months_diff

    data_frame['month_offset'] = data_frame.apply(calculate_offset, axis=1)

    # 4. Count unique active customers per cohort/offset
    cohort_data = data_frame.groupby(['cohort_month', 'month_offset'])['customer_id'].nunique().reset_index()

    # 5. Create pivot table
    cohort_pivot = cohort_data.pivot(index='cohort_month', columns='month_offset', values='customer_id')

    # 6. Calculate retention percentage
    cohort_sizes = cohort_pivot.iloc[:, 0]
    retention_matrix = cohort_pivot.divide(cohort_sizes, axis=0) * 100

    print(retention_matrix.round(2))

cohort_month(data_frame)
