import pandas as pd

ny_house_dataset_master_df = pd.read_csv('NY-House-Dataset.csv')

#print(ny_house_dataset_master_df)

# *Condo for sale*
condo_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,0]
condo_df['Broker Title'] = broker_title.copy()
type = ny_house_dataset_master_df.iloc[:,1]
condo_df['Type'] = type.copy()
price = ny_house_dataset_master_df.iloc[:,2]
condo_df['Price'] = price.copy()
beds = ny_house_dataset_master_df.iloc[:,3]
condo_df['Bedrooms'] = beds.copy() #beds in master df
bath = ny_house_dataset_master_df.iloc[:,4]
condo_df['Bathrooms'] = bath.copy() #bath in master df
condo_df['Bathrooms'] = condo_df['Bathrooms'].astype(int) #convert values from float to int
square_feet = ny_house_dataset_master_df.iloc[:,5]
condo_df['Square Feet'] = square_feet.copy() #bath in master df
condo_df['Square Feet'] = condo_df['Square Feet'].astype(int) #convert values from float to int
address = ny_house_dataset_master_df.iloc[:,6]
condo_df['Address'] = address.copy()
state = ny_house_dataset_master_df.iloc[:,7]
condo_df['State'] = state.copy()
administrative_area_level_2 = ny_house_dataset_master_df.iloc[:,9]
condo_df['Administrative Area Level 2'] = administrative_area_level_2.copy()
locality = ny_house_dataset_master_df.iloc[:,10]
condo_df['Locality'] = locality.copy()
sub_locality = ny_house_dataset_master_df.iloc[:,11]
condo_df['Sub-Locality'] = sub_locality.copy()
latitude = ny_house_dataset_master_df.iloc[:,15]
condo_df['Latitude'] = latitude.copy()
longitude = ny_house_dataset_master_df.iloc[:,16]
condo_df['Longitude'] = longitude.copy()

condo_df.to_csv('condo_df.csv', index=False)

set_res = set(type) #convert TYPE column values to set
# printing out unique elements in TYPE column from sheet of master workbook
print("unique elements in type column from sheet of master workbook:\n")
list_res = (list(set_res))

for item in list_res:
    print(item)

def condo_only_values(df):
    try:
        return df[df['Type'].str.contains('Condo for sale')]
    except Exception as e:
        print('Unable to filter values')

condo_df = condo_only_values(condo_df)

condo_df.to_csv('condo_df.csv', index=False)


# *Co-op for sale*
co_op_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,0]
co_op_df['Broker Title'] = broker_title.copy()
type = ny_house_dataset_master_df.iloc[:,1]
co_op_df['Type'] = type.copy()
price = ny_house_dataset_master_df.iloc[:,2]
co_op_df['Price'] = price.copy()
beds = ny_house_dataset_master_df.iloc[:,3]
co_op_df['Bedrooms'] = beds.copy() #beds in master df
bath = ny_house_dataset_master_df.iloc[:,4]
co_op_df['Bathrooms'] = bath.copy() #bath in master df
co_op_df['Bathrooms'] = co_op_df['Bathrooms'].astype(int) #convert values from float to int
square_feet = ny_house_dataset_master_df.iloc[:,5]
co_op_df['Square Feet'] = square_feet.copy() #bath in master df
co_op_df['Square Feet'] = co_op_df['Square Feet'].astype(int) #convert values from float to int
address = ny_house_dataset_master_df.iloc[:,6]
co_op_df['Address'] = address.copy()
state = ny_house_dataset_master_df.iloc[:,7]
co_op_df['State'] = state.copy()
administrative_area_level_2 = ny_house_dataset_master_df.iloc[:,9]
co_op_df['Administrative Area Level 2'] = administrative_area_level_2.copy()
locality = ny_house_dataset_master_df.iloc[:,10]
co_op_df['Locality'] = locality.copy()
sub_locality = ny_house_dataset_master_df.iloc[:,11]
co_op_df['Sub-Locality'] = sub_locality.copy()
latitude = ny_house_dataset_master_df.iloc[:,15]
co_op_df['Latitude'] = latitude.copy()
longitude = ny_house_dataset_master_df.iloc[:,16]
co_op_df['Longitude'] = longitude.copy()
co_op_df.to_csv('co_op_df.csv', index=False)

def co_op_only_values(df):
    try:
        return df[df['Type'].str.contains('Co-op for sale')]
    except Exception as e:
        print('Unable to filter values')

co_op_df = co_op_only_values(co_op_df)

co_op_df.to_csv('co_op_df.csv', index=False)


# *Multi-family home for sale*
multi_family_home_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,0]
multi_family_home_df['Broker Title'] = broker_title.copy()
type = ny_house_dataset_master_df.iloc[:,1]
multi_family_home_df['Type'] = type.copy()
price = ny_house_dataset_master_df.iloc[:,2]
multi_family_home_df['Price'] = price.copy()
beds = ny_house_dataset_master_df.iloc[:,3]
multi_family_home_df['Bedrooms'] = beds.copy() #beds in master df
bath = ny_house_dataset_master_df.iloc[:,4]
multi_family_home_df['Bathrooms'] = bath.copy() #bath in master df
multi_family_home_df['Bathrooms'] = multi_family_home_df['Bathrooms'].astype(int) #convert values from float to int
square_feet = ny_house_dataset_master_df.iloc[:,5]
multi_family_home_df['Square Feet'] = square_feet.copy() #bath in master df
multi_family_home_df['Square Feet'] = multi_family_home_df['Square Feet'].astype(int) #convert values from float to int
address = ny_house_dataset_master_df.iloc[:,6]
multi_family_home_df['Address'] = address.copy()
state = ny_house_dataset_master_df.iloc[:,7]
multi_family_home_df['State'] = state.copy()
administrative_area_level_2 = ny_house_dataset_master_df.iloc[:,9]
multi_family_home_df['Administrative Area Level 2'] = administrative_area_level_2.copy()
locality = ny_house_dataset_master_df.iloc[:,10]
multi_family_home_df['Locality'] = locality.copy()
sub_locality = ny_house_dataset_master_df.iloc[:,11]
multi_family_home_df['Sub-Locality'] = sub_locality.copy()
latitude = ny_house_dataset_master_df.iloc[:,15]
multi_family_home_df['Latitude'] = latitude.copy()
longitude = ny_house_dataset_master_df.iloc[:,16]
multi_family_home_df['Longitude'] = longitude.copy()
multi_family_home_df.to_csv('multi_family_home_df.csv', index=False)

def multi_family_home_only_values(df):
    try:
        return df[df['Type'].str.contains('Multi-family home for sale')]
    except Exception as e:
        print('Unable to filter values')

multi_family_home_df = multi_family_home_only_values(multi_family_home_df)

multi_family_home_df.to_csv('multi_family_home_df.csv', index=False)


# *Mobile house for sale*
mobile_house_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,0]
mobile_house_df['Broker Title'] = broker_title.copy()
type = ny_house_dataset_master_df.iloc[:,1]
mobile_house_df['Type'] = type.copy()
price = ny_house_dataset_master_df.iloc[:,2]
mobile_house_df['Price'] = price.copy()
beds = ny_house_dataset_master_df.iloc[:,3]
mobile_house_df['Bedrooms'] = beds.copy() #beds in master df
bath = ny_house_dataset_master_df.iloc[:,4]
mobile_house_df['Bathrooms'] = bath.copy() #bath in master df
mobile_house_df['Bathrooms'] = mobile_house_df['Bathrooms'].astype(int) #convert values from float to int
square_feet = ny_house_dataset_master_df.iloc[:,5]
mobile_house_df['Square Feet'] = square_feet.copy() #bath in master df
mobile_house_df['Square Feet'] = mobile_house_df['Square Feet'].astype(int) #convert values from float to int
address = ny_house_dataset_master_df.iloc[:,6]
mobile_house_df['Address'] = address.copy()
state = ny_house_dataset_master_df.iloc[:,7]
mobile_house_df['State'] = state.copy()
administrative_area_level_2 = ny_house_dataset_master_df.iloc[:,9]
mobile_house_df['Administrative Area Level 2'] = administrative_area_level_2.copy()
locality = ny_house_dataset_master_df.iloc[:,10]
mobile_house_df['Locality'] = locality.copy()
sub_locality = ny_house_dataset_master_df.iloc[:,11]
mobile_house_df['Sub-Locality'] = sub_locality.copy()
latitude = ny_house_dataset_master_df.iloc[:,15]
mobile_house_df['Latitude'] = latitude.copy()
longitude = ny_house_dataset_master_df.iloc[:,16]
mobile_house_df['Longitude'] = longitude.copy()
mobile_house_df.to_csv('mobile_house_df.csv', index=False)

def mobile_house_only_values(df):
    try:
        return df[df['Type'].str.contains('Mobile house for sale')]
    except Exception as e:
        print('Unable to filter values')

mobile_house_df = mobile_house_only_values(mobile_house_df)

mobile_house_df.to_csv('mobile_house_df.csv', index=False)


# *Foreclosure*
foreclosure_df = pd.DataFrame()
broker_title = ny_house_dataset_master_df.iloc[:,0]
foreclosure_df['Broker Title'] = broker_title.copy()
type = ny_house_dataset_master_df.iloc[:,1]
foreclosure_df['Type'] = type.copy()
price = ny_house_dataset_master_df.iloc[:,2]
foreclosure_df['Price'] = price.copy()
beds = ny_house_dataset_master_df.iloc[:,3]
foreclosure_df['Bedrooms'] = beds.copy() #beds in master df
bath = ny_house_dataset_master_df.iloc[:,4]
foreclosure_df['Bathrooms'] = bath.copy() #bath in master df
foreclosure_df['Bathrooms'] = foreclosure_df['Bathrooms'].astype(int) #convert values from float to int
square_feet = ny_house_dataset_master_df.iloc[:,5]
foreclosure_df['Square Feet'] = square_feet.copy() #bath in master df
foreclosure_df['Square Feet'] = foreclosure_df['Square Feet'].astype(int) #convert values from float to int
address = ny_house_dataset_master_df.iloc[:,6]
foreclosure_df['Address'] = address.copy()
state = ny_house_dataset_master_df.iloc[:,7]
foreclosure_df['State'] = state.copy()
administrative_area_level_2 = ny_house_dataset_master_df.iloc[:,9]
foreclosure_df['Administrative Area Level 2'] = administrative_area_level_2.copy()
locality = ny_house_dataset_master_df.iloc[:,10]
foreclosure_df['Locality'] = locality.copy()
sub_locality = ny_house_dataset_master_df.iloc[:,11]
foreclosure_df['Sub-Locality'] = sub_locality.copy()
latitude = ny_house_dataset_master_df.iloc[:,15]
foreclosure_df['Latitude'] = latitude.copy()
longitude = ny_house_dataset_master_df.iloc[:,16]
foreclosure_df['Longitude'] = longitude.copy()
foreclosure_df.to_csv('foreclosure_df.csv', index=False)

def foreclosure_only_values(df):
    try:
        return df[df['Type'].str.contains('Foreclosure')]
    except Exception as e:
        print('Unable to filter values')

foreclosure_df = foreclosure_only_values(foreclosure_df)

foreclosure_df.to_csv('foreclosure_df.csv', index=False)


#creating a Details class that will allow us to filter a certain amount of rows
# class Details:
#     def __init__(self, data):
#         pd.set_option('display.max_columns', None)
#         pd.set_option('display.max_rows', None)
#         self.df = pd.read_csv(data)
#     # function created to display head of contents of sheet
#     def print_first_five_rows(self):
#         print(self.df.head())
#     # print any number of rows via head method
#     def print_any_num_of_rows(self, rows): #rows
#         print(self.df.head(rows))
#     def print_columns(self):
#         print(list(self.df.columns))
#     def print_average(self, column):
#         print(f"Average: {column}:", self.df[column].mean())
#
# data = Details('NY-House-Dataset.csv')
#
# print(data.print_first_five_rows())
# print(data.print_any_num_of_rows(15))
# print(data.print_columns())
# print(data.print_average(['PRICE']))