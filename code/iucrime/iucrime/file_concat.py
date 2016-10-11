
# coding: utf-8

# In[5]:

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')
import pandas as pd
import os
import glob


# In[9]:

path = '../../data/offical'
files = glob.glob(os.path.join(path, '*'))


# In[13]:

# read them in
excels = [pd.ExcelFile(name) for name in files]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them.
combined = pd.concat(frames)

# write it out
combined.to_excel(path+"/IU_crime_13-15.xlsx", header=False, index=False)


# In[ ]:



