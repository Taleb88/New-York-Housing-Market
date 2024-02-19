import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

ny_house_dataset_master_df = pd.read_csv('NY-House-Dataset.csv')

print(ny_house_dataset_master_df.head())

condo_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,1]
condo_df['Broker Title'] = broker_title.copy()

condo_df.to_csv('condo_df.csv', index=False)