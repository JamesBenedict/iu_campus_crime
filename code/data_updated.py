import numpy as np
import pandas as pd
import os
import glob
# import geopy
# from geopy.geocoders import Nominatim


path = '../data'
files = glob.glob(os.path.join(path, '*'))
file = path+'/offical/master_iu_crime.csv'


crime_df = pd.read_csv(file, sep=',')

report_num = crime_df['report_num']
date = crime_df['date']
crime= crime_df['crime']
location = crime_df['location']
status = crime_df['status']

location_updates_df = pd.read_csv(path+'/descriptive/location_update.csv', sep=',')

# crime_count = crime.value_counts()
# print(crime_count)