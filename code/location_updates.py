import numpy as np
import pandas as pd
import os
import glob

path = '../data'
files = glob.glob(os.path.join(path, '*'))
file = path+'/offical/master_iu_crime.csv'

crime_df = pd.read_csv(file, sep=',')

location_updates_df = pd.read_csv(path+'/descriptive/location_update.csv', sep=',')
location_dict = location_updates_df.set_index('dirty_location').T.to_dict('list')

for key in location_dict:   
    location_dirty = key
    address = location_dict[key]
    try:
        address = address[0].split(',')
        crime_df.loc[crime_df['location'] == location_dirty, 'lat'] = address[0]
        crime_df.loc[crime_df['location'] == location_dirty, 'long'] = address[1]
        print('tring')
    except AttributeError:
        print('error: can not locate')

crime_df.to_csv(path+"/offical/master_iu_crime.csv", index=False)
