import pandas as pd
from assignment2 import create_grossAmount_net_amount_value_columns
'''
For each category:
compute IQR of 
net_amount
flag outliers (outside [Q1-1.5IQR , Q3+1.5IQR]
cap outliers to bounds (winsorize)
Report outlier counts by category before/after
'''
data_frame = create_grossAmount_net_amount_value_columns()
def IQR_function(data_frame):
    #computing q1 , q3 and iqr
    bounds = data_frame.groupby('category')['net_amount'].quantile([0.25 , 0.75]).unstack()
    bounds.columns = ['Q1' , 'Q3']
    bounds['IQR'] = bounds['Q3'] - bounds['Q1']

    #defining outlier thresholds
    bounds['lower'] = bounds['Q1'] - 1.5*bounds['IQR']
    bounds['upper'] = bounds['Q3'] + 1.5*bounds['IQR']

    #merge them in the dataframe
    data_frame = data_frame.merge(bounds[['lower', 'upper']], left_on='category', right_index=True, how='left')

    #find all outliers
    data_frame['is_outlier'] = (data_frame['net_amount'] < data_frame['lower']) | (data_frame['net_amount'] >  data_frame['upper'])

    #capping outliers instead of deleting them
    data_frame['net_amount_capped'] = data_frame['net_amount'].clip(lower=data_frame['lower'] , upper=data_frame['upper'] ,axis = 0)

    # Before: Count rows flagged as outliers
    before_counts = data_frame[data_frame['is_outlier']].groupby('category').size()

    # After: Recalculate outliers on the capped column (should be 0)
    after_outlier_check = (data_frame['net_amount_capped'] < data_frame['lower']) | (data_frame['net_amount_capped'] > data_frame['upper'])
    after_counts = data_frame[after_outlier_check].groupby('category').size()

    # Summary Report
    report = pd.DataFrame({
        'Outliers_Before': before_counts,
        'Outliers_After': after_counts
    }).fillna(0).astype(int)

    print(report)

IQR_function(data_frame)




