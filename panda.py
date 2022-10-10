import pandas as pd

data = pd.read_csv('/home/kali/Downloads/Telegram Desktop/ds_salaries.csv')

# droping colums
new_data = data.drop('salary_in_usd',axis=1)

# dropping row
new_data = data[data.salary_in_usd != 100000]

# fill Null Value
new_data = data.fillna(data.salary_in_usd.describe().mean())

# drop column with Null value
new_data = data.dropna(axis=1,thresh=0)

# sorting table
new_data = data.sort_values(by='salary_in_usd',ascending=False)

# changing datatypes
data.salary_in_usd.astype(int,errors = 'ignore')
# data.astype()

# reversing the columns
new_data = data[::-1]

# replacing values
new_data = data.replace(['FT',"PT"],[3,0])

# setting index
new_data.set_index('company_size',inplace=True)

# renaming column
new_data = new_data.rename(columns = {'salary':'syal'})

# plotting graph
new_data.plot()

# grouping data
# new_data = data.groupby('company_size',axis=1)

#
