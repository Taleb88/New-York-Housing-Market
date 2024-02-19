import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

ny_house_dataset_master_df = pd.read_csv('NY-House-Dataset.csv')

print(ny_house_dataset_master_df)

condo_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,1]
condo_df['Broker Title'] = broker_title.copy()

condo_df.to_csv('condo_df.csv', index=False)

class Details:
    def __init__(self, data):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data)
    # function created to display head of contents of sheet
    def first_five_rows(self):
        print(self.df.head())

print(Details('NY-House-Dataset.csv'))
