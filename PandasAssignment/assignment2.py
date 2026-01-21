import pandas as pd
'''
Using 
quantity , 
unit_price , 
discount_pct :
compute 
gross_amount = quantity * unit_price 
compute 
net_amount = gross_amount * (1 - discount_pct/100)
Add a 
is_high_value flag (
net_amount > threshold ).
'''
def create_grossAmount_net_amount_value_columns():

    ''' Creates columns in the orders dataframe for gross amount , netamount and ishighvalue. Returns the data frame'''

    data_frame = pd.read_csv("orders.csv" , skipinitialspace = True)
    #print(data_frame)
    data_frame['order_date'] = pd.to_datetime(data_frame['order_date'])
    data_frame['gross_amount'] = data_frame['quantity'] * data_frame['unit_price']
    data_frame['net_amount'] = data_frame['gross_amount'] * (1- data_frame['discount_pct']/100)

    threshold = 10000
    data_frame['is_high_value'] = data_frame['net_amount'].apply(lambda x : True if x > threshold else False)

    #print(f"The data frame after all operations is \n {data_frame}")
    return data_frame

data_frame = create_grossAmount_net_amount_value_columns()
print(data_frame)

