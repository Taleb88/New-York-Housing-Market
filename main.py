import pandas as pd

ny_house_dataset_master_df = pd.read_csv('NY-House-Dataset.csv')

condo_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,1]
condo_df['Broker Title'] = broker_title.copy()

condo_df.to_csv('condo_df.csv', index=False)