import numpy as np
import pandas as pd
import os
import glob

path = '../data'
files = glob.glob(os.path.join(path, '*'))
file = path+'/offical/master_iu_crime.csv'

crime_df = pd.read_csv(file, sep=',')

location_updates_df = pd.read_csv(path+'/descriptive/crime_updates.csv', sep=',')
location_dict = location_updates_df.set_index('crime').T.to_dict('list')

for key in location_dict:   
    crime = key
    crime_class = location_dict[key]
    try:
        crime_df.loc[crime_df['crime'] == crime, 'crime_class'] = crime_class
    except AttributeError:
        print('error: can not classify')

crime_df.to_csv(path+"/offical/master_iu_crime.csv", index=False)
