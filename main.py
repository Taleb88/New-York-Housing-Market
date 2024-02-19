import pandas as pd

ny_house_dataset_master_df = pd.read_csv('NY-House-Dataset.csv')

#print(ny_house_dataset_master_df)

condo_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,1]
condo_df['Broker Title'] = broker_title.copy()

condo_df.to_csv('condo_df.csv', index=False)

#creating a Details class that will allow us to filter a certain amount of rows
class Details:
    def __init__(self, data):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data)
    # function created to display head of contents of sheet
    def print_first_five_rows(self):
        print(self.df.head())
    # print any number of rows via head method
    def print_any_num_of_rows(self, rows): #rows
        print(self.df.head(rows))
    def print_columns(self):
        print(list(self.df.columns))

data = Details('NY-House-Dataset.csv')

print(data.print_first_five_rows())
print(data.print_any_num_of_rows(15))
print(data.print_columns())
