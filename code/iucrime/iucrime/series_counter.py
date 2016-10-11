
# coding: utf-8

# In[1]:

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')
import pandas as pd
import os
import glob


# In[23]:

path = '../../data/'
files = glob.glob(os.path.join(path, '*'))
fpath = path+'offical/IU_crime_13-15.csv'
# manually changed header names
# report_num,date_reported,crime,location,status

crime_df = pd.read_csv(fpath, sep=',')

report_num = crime_df['report_num']
date = crime_df['date_reported']
crime= crime_df['crime']
location = crime_df['location']
status = crime_df['status']

# print(crime_df['crime_class'])
# print(open(fname).read())


# In[25]:

crime_count = crime.value_counts()
crime_count.to_csv(path+'descriptive/crime_count.csv')

loc_count = location.value_counts()
loc_count.to_csv(path+'descriptive/locations_count.csv')


# In[ ]:



