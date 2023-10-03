from pandas.tseries.frequencies import unique
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data['whoAmI']
unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()
for value in unique_values:
  one_hot_data[value] = (data['whoAmI'] == value).astype(int)
print(one_hot_data.head())
# pd.get_dummies(data['whoAmI'])
