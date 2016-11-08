import numpy as np
import pandas as pd
import os
import glob
import geopy
from geopy.geocoders import Nominatim


path = ''
files = glob.glob(os.path.join(path, '*'))
fpath = path+'offical/IU_crime_13-15.csv'



crime_df = pd.read_csv(fpath, sep=',')

report_num = crime_df['report_num']
date = crime_df['date']
crime= crime_df['crime']
location = crime_df['location']
status = crime_df['status']
