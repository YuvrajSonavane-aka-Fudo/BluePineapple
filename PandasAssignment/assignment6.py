import pandas as pd
import numpy as np
'''
Randomly introduce missing values in city, payment_mode, and 
discount_pct.
Apply different strategies: 
fill categorical with “Unknownˮ 
fill numeric with median by  category
Prove it worked: show missing counts before/after.
'''
data_frame = pd.read_csv("orders.csv")
columns_to_add_nan = ["city","payment_mode","discount_pct"]

for i in columns_to_add_nan:
    data_frame.loc[data_frame.sample(frac = 0.2).index , i] = np.nan

print("Missing counts before\n")
print(data_frame)
print(data_frame[columns_to_add_nan].isna().sum())

#strategy 1 . Fill with 'unknown'
data_frame['city'] = data_frame['city'].fillna('Unknown')
data_frame['payment_mode']= data_frame['payment_mode'].fillna('Unknown')

#strategy 2 . Fill with median grouped by category

data_frame['discount_pct'] = data_frame['discount_pct'].fillna(
    data_frame.groupby('category')['discount_pct'].transform('median')
)

print("Data after filling nan \n")
print(data_frame)
print(data_frame[columns_to_add_nan].isna().sum())
